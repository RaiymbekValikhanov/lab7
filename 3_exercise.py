import pygame
import math

ScreenWidth = 800
ScreenHeight = 600
CenterX = ScreenWidth // 2
CenterY = ScreenHeight // 2
Game = True

n = 5
R = 200
r = 75
angle = 360 // n
out_vertices = []
in_vertices = []

for i in range(0, 360, angle):
    ang = i * math.pi / 180
    x = r * math.sin(ang) + CenterX
    y = CenterY + r * math.cos(ang)
    in_vertices.append((x, y))
for i in range(0, 360, angle):
    ang = i * math.pi / 180
    x = R * math.sin(ang) + CenterX
    y = CenterY - R * math.cos(ang)
    out_vertices.append((x, y))
out_vertices = out_vertices[0:1] + list(reversed(out_vertices[1::]))
in_vertices = in_vertices[2::] + in_vertices[0:2]
in_vertices.append(in_vertices[0])

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()

for i in range(n):
    a = out_vertices[i]
    b, c = in_vertices[i], in_vertices[i + 1]
    # use pygame.draw.polygon
    pygame.draw.polygon(background, (0,180,0), (a, b, c), 5)
screen.blit(background, (0, 0))

while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
    pygame.display.update()

pygame.quit()
