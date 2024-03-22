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
