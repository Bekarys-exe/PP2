import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game")

CELL_SIZE = 20
SCORE_FONT = pygame.font.Font(None, 26)

# Функция отрисовки змейки
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

# Функция создания еды, чтобы не попадала на змейку
def generate_food(snake):
    while True:
        food = (random.randint(1, 28) * CELL_SIZE,
                random.randint(1, 17) * CELL_SIZE)
        if food not in snake:
            return food, pygame.time.get_ticks()  # Возвращаем еду и текущее время

clock = pygame.time.Clock()
snake = [(600 // 2, 400 // 2)]
direction = (CELL_SIZE, 0)
food, food_timer = generate_food(snake)
running = True
score = 0
level = 1
speed = 10
game_over = False

# Определение стен
walls = [
    (0, 360, CELL_SIZE * 10, CELL_SIZE),  # Нижняя левая
    (400, 360, CELL_SIZE * 10, CELL_SIZE),  # Нижняя правая
    (0, 0, CELL_SIZE * 10, CELL_SIZE),  # Верхняя левая
    (400, 0, CELL_SIZE * 10, CELL_SIZE),  # Верхняя правая
    (180, 380, CELL_SIZE, CELL_SIZE),
    (400, 380, CELL_SIZE, CELL_SIZE),
    (0, 20, CELL_SIZE, CELL_SIZE * 5),
    (580, 20, CELL_SIZE, CELL_SIZE * 5),
    (0, 260, CELL_SIZE, CELL_SIZE * 5),
    (580, 260, CELL_SIZE, CELL_SIZE * 5)
]

while running:
    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    
    # Лаб 9 , проверка истечения 10 секунд для еды
    if current_time - food_timer > 10000:  # 10 секунд = 10000 миллисекунд
        food, food_timer = generate_food(snake)
    
    # Отображение счета и уровня
    screen.blit(SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255)), (0, 380))
    screen.blit(SCORE_FONT.render(f"Level: {level}", True, (255, 255, 255)), (420, 380))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w] and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key in [pygame.K_DOWN, pygame.K_s] and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key in [pygame.K_LEFT, pygame.K_a] and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key in [pygame.K_RIGHT, pygame.K_d] and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
    
    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    # Телепортация при выходе за границы
    new_head = (
        new_head[0] % 600,
        new_head[1] % 400,
    )
    
    # Проверка столкновения с самой собой
    if new_head in snake:
        game_over = True
    
    # Проверка столкновения со стенами
    for wall in walls:
        if wall[0] <= new_head[0] < wall[0] + wall[2] and wall[1] <= new_head[1] < wall[1] + wall[3]:
            game_over = True
    
    if game_over:
        break
    
    snake.insert(0, new_head)
        
    # Проверка еды
    if new_head == food: # поедание еды змейкой
        score += random.randint(1, 5) # Лаб 9 рандомный вес для еды 
        food, food_timer = generate_food(snake)  # Генерируем новую еду
        
        # Увеличение уровня каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2  # Увеличение скорости
    else:
        snake.pop() # Если не съедена , змейка движется без роста

    # Отрисовка змейки и еды
    draw_snake(snake)
    pygame.draw.rect(screen, (255, 0, 0), (*food, CELL_SIZE, CELL_SIZE))
    
    # Отрисовка стен
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall)
    #обновление экрана и ограничение FPS
    pygame.display.flip()
    clock.tick(speed)

# Завершение игры
screen.blit(SCORE_FONT.render(f"GAME OVER", True, (125, 0, 0)), (245, 0))
pygame.display.flip()
pygame.time.delay(2000)
pygame.quit()