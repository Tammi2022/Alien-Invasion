import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 飞船发射的子弹
    def __init__(self, ai_settings, screen, ship):
        # 在飞船所处的位置创建一个子弹对象
        # super(Bullet, self).__init__() python2.7的语法，适用于python3，下面这句简写
        super().__init__()
        self.screen = screen

        # 在0,0处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
