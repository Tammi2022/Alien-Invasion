import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        url_img = "images/rocket.webp"
        image = pygame.image.load(url_img)
        self.image = pygame.transform.scale(image, (80, 100))  # 缩放图像
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # self.center = float(self.rect.centerx)  # 在飞船的属性center中存储小数值
        self.center_x = float(self.rect.centerx)  # 在飞船的属性center中存储小数值
        self.center_y = float(self.rect.centery)  # 在飞船的属性center中存储小数值

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def update_old(self):
        # 根据移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.center += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def update(self):
        # 根据移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:  # 飞船向上移动且未到达屏幕顶部
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # 飞船向下移动且未到达屏幕底部
            self.center_y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y
