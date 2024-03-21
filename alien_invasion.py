import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)  # 创建一艘飞船
    bullets = Group()  # 创建一个用于存储子弹的编组

    while True:  # 开始游戏主循环
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
