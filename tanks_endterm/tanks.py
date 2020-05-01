import pygame
import math
from random import randint as rnd

pygame.init()
FieldWidth = 800
FieldHeight = 600
White = (255, 255, 255)
Grey = (150, 150, 150)
Red = (255, 0, 0)
Green = (0, 255, 0)
Black = (0, 0, 0)

class BattleField:
    def __init__(self):
        self.width = FieldWidth
        self.height = FieldHeight
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.main_sur = pygame.image.load('field.png')
        self.screen.fill(White)
        self.map = [pygame.Rect(90, 190, 200, 45),
                    pygame.Rect(490, 90, 95, 95),
                    pygame.Rect(190, 390, 100, 100),
                    pygame.Rect(500, 340, 190, 45)]
        self.font = pygame.font.Font(None, 36)
        self.start = self.font.render('PRESS SPACE + M TO START', True, Red, White)
        self.start_rect = self.start.get_rect()
        self.start_rect.center = (self.width // 2, self.height // 2)
        self.play_sound = pygame.mixer.Sound('play.wav')

    def draw(self, sur, x, y):
        self.screen.blit(sur, (x, y))

    def text(self, res):
        result = self.font.render(res, True, Red, White)
        res_rect = result.get_rect()
        res_rect.center = (self.width // 2, self.height // 2)
        return result



class Tank:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.ds = 5
        self.angle = rnd(0, 360)
        self.speed = 20
        self.avatar = pygame.image.load(image).convert_alpha()
        self.size = self.avatar.get_rect().width
        self.nose_l = self.size / 2 - self.ds
        self.nose_x = 0
        self.nose_y = self.nose_l
        self.sound = pygame.mixer.Sound('shot.wav')
        self.hp = 3

    def rotation(self, rt, sec):
        self.angle = self.angle + round(2 * rt * self.speed * sec)
        ang_rad = self.angle * math.pi / 180
        self.nose_x = self.nose_l * math.sin(ang_rad)
        self.nose_y = self.nose_l * math.cos(ang_rad)

    def movement(self, dr, sec, field):
        ang_rad = self.angle * math.pi / 180
        dx = dr * 2 * self.speed * math.sin(ang_rad) * sec
        dy = dr * 2 * self.speed * math.cos(ang_rad) * sec
        self.x = self.x + dx
        for rect in field.map:
            if pygame.Rect.colliderect(rect, self.get_r()):
                self.x -= dx
        self.y = self.y + dy
        for rect in field.map:
            if pygame.Rect.colliderect(rect, self.get_r()):
                self.y -= dy
        if self.x + self.ds > FieldWidth: self.x = self.ds - self.size
        if self.x + self.size - self.ds < 0: self.x = FieldWidth - self.ds
        if self.y + self.ds > FieldHeight: self.y = self.ds - self.size
        if self.y + self.size - self.ds < 0: self.y = FieldHeight - self.ds

    def get_r(self):
        return (self.x + self.ds, self.y + self.ds,
                self.size - 2 * self.ds, self.size - 2 * self.ds)


class Bullet:
    def __init__(self, x, y, angle):
        self.r = 5
        self.speed = 100
        self.x = x
        self.y = y
        self.d_x = 1
        self.d_y = 1
        self.dist = 0
        self.angle = angle
        self.bullet = pygame.image.load('bullet.png')

    def get_r(self):
        return pygame.Rect((self.x, self.y,
                            self.r, self.r))

    def move(self, sec, field):
        ang_rad = self.angle * math.pi / 180
        dx = self.d_x * self.speed * math.sin(ang_rad) * sec
        dy = self.d_y * self.speed * math.cos(ang_rad) * sec
        self.x -= dx
        for rect in field.map:
            if pygame.Rect.colliderect(rect, self.get_r()):
                self.d_x = -self.d_x
                self.x += dx
        self.y -= dy
        for rect in field.map:
            if pygame.Rect.colliderect(rect, self.get_r()):
                self.d_y = -self.d_y
                self.y += dy

        self.dist += (dx ** 2 + dy ** 2) ** 0.5
        if self.x > FieldWidth: self.x = 0
        if self.x < 0: self.x = FieldWidth
        if self.y > FieldHeight: self.y = 0
        if self.y < 0: self.y = FieldHeight


def rotate_image(image, ang):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, ang)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

field = BattleField()

def play():

    game = True
    tank1 = Tank(50, 50, 'tank1.png')
    tank2 = Tank(700, 500,'tank2.png')
    clock = pygame.time.Clock()
    last_now1 = pygame.time.get_ticks()
    last_now2 = pygame.time.get_ticks()
    bullets = []
    recharge = 2000


    while game:

        field.draw(field.main_sur, 0, 0)
        dt = clock.tick(30) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: tank1.rotation(1, dt)
        if keys[pygame.K_d]: tank1.rotation(-1, dt)
        if keys[pygame.K_w]: tank1.movement(-1, dt, field)
        if keys[pygame.K_s]: tank1.movement(1, dt, field)
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - last_now1 >= recharge:
                tank1.sound.play()
                bullets.append(Bullet(tank1.x + tank1.size / 2 - tank1.nose_x,
                                      tank1.y + tank1.size / 2 - tank1.nose_y, tank1.angle))
                last_now1 = now

        if keys[pygame.K_LEFT]: tank2.rotation(1, dt)
        if keys[pygame.K_RIGHT]: tank2.rotation(-1, dt)
        if keys[pygame.K_UP]: tank2.movement(-1, dt, field)
        if keys[pygame.K_DOWN]: tank2.movement(1, dt, field)
        if keys[pygame.K_m]:
            now = pygame.time.get_ticks()
            if now - last_now2 >= recharge:
                tank2.sound.play()
                bullets.append(Bullet(tank2.x + tank2.size / 2 - tank2.nose_x,
                                      tank2.y + tank2.size / 2 - tank2.nose_y, tank2.angle))
                last_now2 = now

        for bullet in bullets:
            bullet.move(dt, field)
            if pygame.Rect.colliderect(bullet.get_r(), tank1.get_r()) and bullet.dist > 10:
                tank1.hp -= 1
                bullets.remove(bullet)
                if tank1.hp == 0:
                    return "SECOND PLAYER WIN (PRESS R TO RESTART)"
            if pygame.Rect.colliderect(bullet.get_r(), tank2.get_r()) and bullet.dist > 10:
                tank2.hp -= 1
                bullets.remove(bullet)
                if tank2.hp == 0:
                    return "FIRST PLAYER WIN (PRESS R TO RESTART)"

            if bullet.dist > 1000:
                bullets.remove(bullet)
            field.draw(bullet.bullet, bullet.x, bullet.y)
        score1 = field.font.render("1HP:" + str(tank1.hp), True, Green).convert_alpha()
        score2 = field.font.render("2HP:" + str(tank2.hp), True, Red).convert_alpha()

        field.draw(rotate_image(tank1.avatar, tank1.angle), tank1.x, tank1.y)
        field.draw(rotate_image(tank2.avatar, tank2.angle), tank2.x, tank2.y)
        field.draw(score1, 0, 0)
        field.draw(score2, 700, 0)
        pygame.display.flip()

    pygame.quit()

def main():
    sur = field.start
    field.play_sound.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and keys[pygame.K_m]:
            result = play()
            sur = field.text(result)
        if keys[pygame.K_r]:
            sur = field.start
        field.screen.fill(White)
        field.screen.blit(sur, field.start_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
