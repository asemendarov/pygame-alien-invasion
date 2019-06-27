import pygame

from pygame.sprite import Group

from ship import Ship
from bullet import Bullet
from settings import Settings
from event_handling import EventHandling


def run_game(settings):
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    # Создание группы для хранения пуль
    bullets = Group()

    ship = Ship(screen=screen, speed_ship=(1, 1, 1, 1))
    bullet = Bullet(screen=screen, ship=ship, bullets=bullets, bullet_speed_factor=1,
                    bullet_width=3, bullet_height=15, bullet_color=(60, 60, 60))
    event_handling = EventHandling(ship, bullet)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        event_handling.processing_events()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(settings.bg_color)
        ship.update()
        ship.blitme()

        bullets.update()

        # Все пули выводятся позади изображений корабля и пришельцев
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        # Удаление пуль, вышедших за край экрана
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


def main():
    # Инициируем игру и создаем объект экрана
    pygame.init()

    # Запускаем игру
    run_game(Settings(
        title='Alien Invasion',
        size=(1200, 800),
        color=(230, 230, 230)
    ))


if __name__ == '__main__':
    main()
