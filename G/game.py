import pygame

pygame.init()

pygame.display.set_mode((720, 480))

events = pygame.event.get()

while 1:
    for i in events():
        if i.type == pygame.QUIT:
            pygame.quit()`
