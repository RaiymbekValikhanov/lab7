import pygame
import math

ScreenWidth = 800
ScreenHeight = 600
CenterX = ScreenWidth // 2
CenterY = ScreenHeight // 2
Game = True

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()
pygame.draw.arc(background, (0,150,0),(0, 0, 2 * ScreenWidth, 2 * ScreenHeight), math.pi / 2, math.pi, 3)
screen.blit(background, (0, 0))


while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
    pygame.display.update()

pygame.quit()
