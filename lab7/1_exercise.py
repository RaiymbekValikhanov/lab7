import pygame

ScreenWidth = 800
ScreenHeight = 600
Game = True

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()
screen.blit(background, (0, 0))

ball_r = 300
ball_surface = pygame.Surface((2 * ball_r, 2 * ball_r))
ball_surface.fill((255, 255, 255))
ball = pygame.draw.circle(ball_surface, (255, 0, 255), (ball_r, ball_r), ball_r)
screen.blit(ball_surface, (ScreenWidth // 2 - ball_r, ScreenHeight // 2 - ball_r))

while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
    pygame.display.update()
    
pygame.quit()
