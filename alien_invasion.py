import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = (alien.rect.width)/2
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)  # 创建一艘飞船
    bullets = Group()  # 创建一个用于存储子弹的编组
    # alien = Alien(ai_settings, screen)  # 创建一个外星人
    aliens = Group()  # 创建一个外星人

    while True:  # 开始游戏主循环
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # bullets.update()
        # for bullet in bullets:
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
