import sys
import pygame
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # bg_color = (230, 230, 230)  # 浅灰色
    # 红色(255, 0, 0) 绿色(0, 255, 0) 蓝色(0, 0, 255)

    while True:
        # screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()
