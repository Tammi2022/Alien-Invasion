import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)  # 创建一个用于存储游戏统计信息的实例
    sb = Scoreboard(ai_settings, screen, stats)  # 创建存储游戏统计信息的实例，并创建记分牌
    ship = Ship(ai_settings, screen)  # 创建一艘飞船
    bullets = Group()  # 创建一个用于存储子弹的编组
    # alien = Alien(ai_settings, screen)  # 创建一个外星人
    aliens = Group()
    play_button = Button(ai_settings, screen, "Play")

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:  # 开始游戏主循环
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            # bullets.update()
            # for bullet in bullets:
            #     if bullet.rect.bottom <= 0:
            #         bullets.remove(bullet)
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
