import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()  # 快捷键Q来结束游戏


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 更新屏幕上的图像，并切换到新屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bulltes):
    bulltes.update()  # 更新子弹的位置
    for bullte in bulltes.copy():
        if bullte.rect.bottom <= 0:
            bulltes.remove(bullte)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bulltes)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bulltes):
    # 检查是否有子弹击中了外星人
    # 如果是则删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bulltes, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bulltes.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bulltes中
    if len(bullets) < ai_settings.bullets_allowed:  # 限制条件
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    # 计算每行可容纳多少个外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算屏幕每行可容纳多少行外星人
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)  # 检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    aliens.update()  # 更新外星人群中所有外星人的位置
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    # 有外星人到达边缘时采取相应的措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    # 将整群外星人下移，并改变它们的方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    # 响应被外星人撞到的飞船
    stats.ships_left -= 1  # 将ship_left减1

    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，并将飞船放到屏幕底端中央
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # 暂停
    sleep(0.5)
