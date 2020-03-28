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
for point in range(0,ScreenHeight,1):
    cl = point * 255 // 600
    pygame.draw.line(background, (255,cl,0), (0,0), (ScreenWidth, point), 1)
    pygame.draw.line(background, (0, cl, 255), (0, ScreenHeight), (ScreenWidth, point), 1)
    pygame.draw.line(background, (0, 255, cl), (ScreenWidth, 0), (0, point), 1)
    pygame.draw.line(background, (255, 0, cl), (ScreenWidth, ScreenHeight), (0, point), 1)
screen.blit(background, (0, 0))

while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
    pygame.display.update()

pygame.quit()
