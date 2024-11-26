import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0,0,0))

x = 100

y = 50

for a in range(10):
    for x in range(1, 11):
        naytto.blit(robo, (x*50+a*5, y))

    y += 15

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()