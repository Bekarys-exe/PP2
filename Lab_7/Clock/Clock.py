import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()


display = pygame.image.load("chasibezstrelok9.jpg")
background = pygame.image.load("Bill_Cipher.png")
minute_hand = pygame.image.load("Bill_Cipher_Left_Hand.png")
second_hand = pygame.image.load("Bill_Cipher_Right_Hand.png")

def blit_rotate_center(surf, image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(display, (0, 0))

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -minutes * 6 - 90
    second_angle = -seconds * 6 + 90

    center = (350, 350)

    blit_rotate_center(screen, minute_hand, minute_angle, center)
    blit_rotate_center(screen, second_hand, second_angle, center)
    screen.blit(background, (130, 130))

    pygame.display.flip()
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()