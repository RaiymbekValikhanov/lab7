import pygame
import math

ScreenWidth = 800
ScreenHeight = 600
CenterX = ScreenWidth // 2
CenterY = ScreenHeight // 2
Game = True

n = 5
R = 300
r = 75
angle = 360 // n
out_vertices = []

for i in range(0, 360, angle):
    ang = i * math.pi / 180
    x = R * math.sin(ang) + CenterX
    y = CenterY - R * math.cos(ang)
    out_vertices.append((x, y))

out_vertices = out_vertices[0::2] + out_vertices[1::2]
pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
pygame.draw.polygon(background, (0,180,0), out_vertices, 5)
background = background.convert()

screen.blit(background, (0, 0))

while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
    pygame.display.update()

pygame.quit()
