import pygame
import random
import sys

pygame.init()

naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

robot_count = 1000

robot_positions = [
    (random.randint(0, 640 - robo.get_width()), random.randint(0, 480 - robo.get_height()))
    for _ in range(robot_count)
]

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    naytto.fill((0, 0, 0))

    for position in robot_positions:
        naytto.blit(robo, position)

    pygame.display.flip()