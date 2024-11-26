import pygame

pygame.init()

naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
y = 0
speed = 2

direction = 'right'

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    naytto.fill((0, 0, 0))

    if direction == 'right':
        x += speed
        if x + robo.get_width() >= 640:
            direction = 'down'
    elif direction == 'down':
        y += speed
        if y + robo.get_height() >= 480:
            direction = 'left'
    elif direction == 'left':
        x -= speed
        if x <= 0:
            direction = 'up'
    elif direction == 'up':
        y -= speed
        if y <= 0:
            direction = 'right'

    naytto.blit(robo, (x, y))
    pygame.display.flip()

    kello.tick(60)