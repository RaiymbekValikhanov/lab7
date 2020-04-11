import pygame
import math

ScreenWidth = 812
ScreenHeight = 612
CenterX = ScreenWidth // 2
CenterY = ScreenHeight // 2
Radius = 25
Color = (255, 0, 0)

class Field(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

    def circle(self, x, y, radius):
        diameter = 2 * radius
        surface = pygame.Surface((diameter, diameter))
        pygame.draw.circle(surface, Color, (radius, radius), radius)
        surface.set_colorkey((0, 0, 0))
        self.screen.blit(surface.convert_alpha(),(x - radius, y - radius))

    def run(self, draw):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            draw()
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()


class Ball(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.dx = 20
        self.dy = 20

    def move(self, direct_x, direct_y):
        self.x = self.x + direct_x * self.dx
        self.y = self.y + direct_y * self.dy
        if self.x - self.r < 0 or self.x + self.r > ScreenWidth:
            self.x = self.x - direct_x * self.dx
        if self.y - self.r < 0 or self.y + self.r > ScreenHeight:
            self.y = self.y - direct_y * self.dy

    def draw(self, view):
        view.circle(self.x, self.y, self.r)


def action(ball, view):
    def animate():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ball.move(-1, 0)
        if keys[pygame.K_d]:
            ball.move(1, 0)
        if keys[pygame.K_w]:
            ball.move(0, -1)
        if keys[pygame.K_s]:
            ball.move(0, 1)
        ball.draw(view)
    return animate

def main():
    ball = Ball(CenterX, CenterY, Radius)
    view = Field(ScreenWidth, ScreenHeight)
    view.run(action(ball, view))

if __name__ == '__main__':
    main()
