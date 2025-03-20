import pygame

pygame.init()

screen = pygame.display.set_mode((640 ,640))

clock = pygame.time.Clock()

done = False

x = 100
y = 100
radius = 25
speed = 20
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and x + radius + speed <= 640 : x += speed
    if pressed[pygame.K_LEFT] and x - radius - speed >= 0 : x -= speed
    if pressed[pygame.K_UP] and y - radius - speed >= 0 : y -= speed
    if pressed[pygame.K_DOWN] and y + radius + speed <= 640 : y += speed
    
    screen.fill((255 , 255 , 255))
    pygame.draw.circle( screen , (255 , 0 , 0) , (x , y) , radius) 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()        