import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        # super().__init__()
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        url_img = "images/alien.webp"
        image = pygame.image.load(url_img)
        self.image = pygame.transform.scale(image, (80, 100))  # 缩放图像
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)  # 存储外星人的准确位置
        self.y = float(self.rect.y)  # 存储外星人的准确位置

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 在指定位置绘制外星人

    def update(self):
        # 向左或向右移动外星人
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        # self.x += self.ai_settings.alien_speed_factor  # 向右移动外星人
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        # 如果外星人位于屏幕边缘，就返回True
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
