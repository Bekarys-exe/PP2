import pygame
import random

# Инициализация Pygame и микшера звука
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Race")

# Создание игрового окна
screen = pygame.display.set_mode((312, 400))
FPS = pygame.time.Clock()

# Загрузка шрифтов
font = pygame.font.Font(None, 40)  # Основной шрифт
score_font = pygame.font.Font(None, 20)  # Шрифт для счёта

# Загрузка изображений
road = pygame.image.load("road.png")
player = pygame.image.load("WhiteStrip.png")
enemys = [
    pygame.image.load("BlackOut.png"),
    pygame.image.load("BlueStrip.png"),
    pygame.image.load("GreenStrip.png"),
    pygame.image.load("PinkStrip.png"),
    pygame.image.load("RedStrip.png")
]
coin = pygame.image.load("coin_16x16.png")
sound_icon = [pygame.image.load("unmute_s.png"), pygame.image.load("mute_s.png")]
music_icon = [pygame.image.load("unmute_m.png"), pygame.image.load("mute_m.png")]

# Загрузка и воспроизведение фоновой музыки в бесконечном цикле
pygame.mixer.music.load("MAX-COVERI-RUNNING-IN-THE-90S-頭文字D-INITIAL-D.mp3")
pygame.mixer.music.play(-1)

# Загрузка звуковых эффектов
sounds = [
    pygame.mixer.Sound("mixkit-retro-arcade-game-over-470.wav"),  # Звук проигрыша
    pygame.mixer.Sound("mixkit-winning-a-coin-video-game-2069.wav")  # Звук подбора монеты
]

# Игровые переменные
speed = 5  # Скорость движения объектов
road_pos = 0  # Позиция дороги (для эффекта движения)
player_pos = 124  # Начальная позиция игрока
speed_mem = 0  # Запоминание скорости при паузе
accel = 0.1  # Ускорение игры
last_accel_time = 0  # Время последнего ускорения
score = 0  # Очки
coin_score = 0  # Количество собранных монет
GO = False  # Флаг окончания игры
sound = True  # Флаг звука
music = True  # Флаг музыки
played = False  # Флаг проигрывания звука проигрыша
pause_title = False  # Флаг паузы
coin_speed = False # Повышает скорость при подборе 10 монет

# Класс для вражеских машин и монет
class enemy_car():
    def __init__(self):
        self.row = random.randint(0, 2)  # Полоса движения врага
        self.color = random.randint(0, 4)  # Цвет машины
        self.y = -64  # Начальная позиция
        self.m_row = 3  # Полоса появления монеты
        self.coin_collected = False  # Флаг собранной монеты
        
        # Выбираем полосу для монеты, чтобы она не совпадала с врагом
        while self.m_row == self.row or self.m_row == 3:
            self.m_row = random.randint(0, 2)

    def movement(self):
        global GO, coin_score, coin_speed
        self.y += speed

        if self.y < 464:
            screen.blit(enemys[self.color], (103 * self.row + 21, self.y))
            
            # Проверка на столкновение с врагом
            if (236 <= self.y <= 336) and (player_pos - 32 <= 103 * self.row + 21 <= player_pos + 32):
                GO = True
            
            # Если монета не собрана, рисуем её
            if not self.coin_collected:
                screen.blit(coin, (103 * self.m_row + 45, self.y))
                if (284 <= self.y <= 364) and (player_pos - 8 <= 103 * self.m_row + 37 <= player_pos + 40):
                    self.coin_collected = True  # Монета подобрана
                    sounds[1].play()
                    coin_score += random.randint(1, 5)  # Увеличиваем счёт монет # Lab 9  , разный вес монет
                    if coin_score % 10 == 0:
                        coin_speed = True
        else:
            # Респавн врага
            self.__init__()

car = enemy_car()

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            music = not music
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            sound = not sound
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause_title = not pause_title
            if speed != 0:  # Если игра не на паузе, ставим на паузу
                speed_mem = speed
                speed = 0
                accel = 0
            else:  # Если уже на паузе, снимаем паузу
                speed = speed_mem
                accel = 0.1
                last_accel_time = current_time  # Сброс таймера для корректного увеличения счёта

    # Движение дороги
    road_pos = (road_pos + speed) % 400
    screen.blit(road, (0, road_pos))
    screen.blit(road, (0, road_pos - 400))

    # Управление машиной
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and player_pos - speed >= 0:
        player_pos -= speed
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and player_pos + speed <= 248:
        player_pos += speed
    screen.blit(player, (player_pos, 300))

    # Движение врага и проверка столкновений
    car.movement()

    # Отображение надписи PAUSE при паузе
    if pause_title:
        screen.blit(font.render("PAUSE", True, (255, 255, 0)), (10, 0))

    # Обработка окончания игры
    if GO:
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (10, 0))
        speed = 0
        if not played:
            sounds[0].play()
            played = True

    # Ускорение игры каждую секунду (если нет паузы и игра не окончена)
    if not GO and not pause_title and current_time - last_accel_time > 1000:
        score += 1
        speed += accel
        last_accel_time = current_time

    # Увеличение скорости при подборе 10 монет врагов , # Lab 9
    if coin_speed:
        speed += 10 * accel
        coin_speed = False

    # Отображение счёта
    screen.blit(score_font.render(f"SCORE: {score}", True, (255, 255, 255)), (4, 24))
    screen.blit(score_font.render(f"COINS: {coin_score}", True, (255, 255, 255)), (225, 24))

    # Включение и выключение звука/музыки
    pygame.mixer.music.set_volume(1 if music else 0)
    screen.blit(music_icon[0 if music else 1], (277, 368))
    sounds[1].set_volume(0.5 if sound else 0)
    sounds[0].set_volume(1 if sound else 0)
    screen.blit(sound_icon[0 if sound else 1], (3, 368))

    FPS.tick(60)
    pygame.display.update()

pygame.quit()