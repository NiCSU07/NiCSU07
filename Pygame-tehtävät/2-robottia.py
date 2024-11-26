import pygame
import os



pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo_ylo = pygame.image.load("robo.png")
robo_alo = pygame.image.load("robo.png")
   
    

ylo_x = 0
ylo_y = 100
alo_x = 0
alo_y = 300
ylo_nopeus = 1
alo_nopeus = 2
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    naytto.fill((0, 0, 0))

    naytto.blit(robo_ylo, (ylo_x, ylo_y))
    naytto.blit(robo_alo, (alo_x, alo_y))
    
    pygame.display.flip()

    ylo_x += ylo_nopeus
    alo_x += alo_nopeus

    if ylo_nopeus > 0 and ylo_x + robo_ylo.get_width() >= 640:
        ylo_nopeus = -ylo_nopeus
    elif ylo_nopeus < 0 and ylo_x <= 0:
        ylo_nopeus = -ylo_nopeus

    if alo_nopeus > 0 and alo_x + robo_alo.get_width() >= 640:
        alo_nopeus = -alo_nopeus
    elif alo_nopeus < 0 and alo_x <= 0:
        alo_nopeus = -alo_nopeus

    kello.tick(60)