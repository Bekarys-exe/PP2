import pygame

pygame.init()

screen = pygame.display.set_mode((600 , 600))

clock = pygame.time.Clock()

done = False

playlist = ['SoloL.mp3' , 'AntK.mp3' , 'F.mp3' ]
current_track = 0
Player_image = pygame.image.load('Player.webp').convert_alpha()
Player_image = pygame.transform.scale(Player_image , (450 , 450))

while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1 :
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2 :
            pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3 :  
            current_track = (current_track -1) % len(playlist)
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4 :
            current_track = (current_track +1) % len(playlist)
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_7 :
            pygame.mixer.music.set_volume(0.5)    

    screen.fill((255 , 255 , 255))
    screen.blit(  Player_image,  ( 50 , 50))     
    print(playlist[current_track])
    pygame.display.flip()
    clock.tick(5)

pygame.quit()                     