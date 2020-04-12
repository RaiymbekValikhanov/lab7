import pygame
from random import randint as rnd

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
        self.fps = 5
        self.cleanup = True
        self.wild = False
        self.clock = pygame.time.Clock()

    def wild_paint(self):
        pygame.draw.circle(self.background, (rnd(0,255), rnd(0,255),rnd(0,255)),
                           (rnd(0, self.width), rnd(0, self.height)), rnd(50, 500))

    def circle(self, x, y, radius):
        diameter = 2 * radius
        surface = pygame.Surface((diameter, diameter))
        pygame.draw.circle(surface, Color, (radius, radius), radius)
        surface.set_colorkey((0, 0, 0))
        self.screen.blit(surface.convert_alpha(),(x - radius, y - radius))

    def change(self, key):
        if key == pygame.K_1:
            self.fps = 5
        elif key == pygame.K_2:
            self.fps = 10
        elif key == pygame.K_3:
            self.fps = 20
        elif key == pygame.K_4:
            self.fps = 30
        elif key == pygame.K_5:
            self.fps = 60
        elif key == pygame.K_x:
            self.wild = not self.wild
        elif key == pygame.K_y:
            self.cleanup = not self.cleanup
        elif key == pygame.K_w:
            self.background.fill((255, 255, 255))
            self.wild = False

    def run(self, draw):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                elif event.type == pygame.KEYDOWN:
                    self.change(event.key)
            if self.wild:
                self.wild_paint()
            if self.cleanup:
                self.screen.blit(self.background, (0, 0))
            draw()
            pygame.display.set_caption("%.3f" % self.clock.get_fps())
            pygame.display.update()


        pygame.quit()

class Ball(object):
    def __init__(self):
        self.x = CenterX
        self.y = CenterY
        self.r = 25
        self.dx = rnd(50, 100)
        self.dy = rnd(50, 100)

    def move(self, sec):
        self.x += self.dx * sec
        self.y += self.dy * sec
        if self.x - self.r < 0 or self.x + self.r > ScreenWidth:
            self.dx *= -1
        if self.y - self.r < 0 or self.y + self.r > ScreenHeight:
            self.dy *= -1

    def draw(self, view):
        view.circle(self.x, self.y, self.r)

def action(ball, view):
    def animate():
        sec = view.clock.tick(view.fps) / 1000
        ball.move(sec)
        ball.draw(view)
    return animate

def main():
    ball = Ball()
    view = Field(ScreenWidth, ScreenHeight)
    view.run(action(ball, view))

if __name__ == '__main__':
    main()
