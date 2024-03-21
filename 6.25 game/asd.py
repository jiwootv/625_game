import pygame, data.code.save
import time

SIZE = width, height = 640, 240

screen = pygame.display.set_mode(SIZE)
screen.fill((255, 255, 255))
pygame.init()
print()
S = data.code.save.Save()

print(S.is_none(0))
