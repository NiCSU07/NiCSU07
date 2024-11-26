import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0,0,0))
leveys = robo.get_width()
korkeus = robo.get_height()
naytto.blit(robo, (30-leveys/2, 45-korkeus/2))
naytto.blit(robo, (30-leveys/2, 430-korkeus/2))
naytto.blit(robo, (610-leveys/2, 45-korkeus/2))
naytto.blit(robo, (610-leveys/2, 430-korkeus/2))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()