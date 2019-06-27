import pygame

from pygame.sprite import Group

from ship import Ship, EventHandlingStandardShip
from bullet import Bullet, GroupBullet, EventHandlingStandardBullet
from settings import Settings
from event_handling import EventHandling


def run_game(settings):
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    # Создание космического корабля и пули
    ship = Ship(screen=screen, speed_ship=(1, 1, 1, 1))
    bullet = Bullet(screen=screen, ship=ship, bullet_speed_factor=1,
                    bullet_width=3, bullet_height=15, bullet_color=(60, 60, 60))

    # Создание группы для хранения пуль
    group_bullet = GroupBullet(Group(), bullet)

    # Создание обработчика для космического корабля и пуль
    handling_bullet = EventHandlingStandardBullet(group_bullet)
    handling_ship = EventHandlingStandardShip(ship)
    event_handling = EventHandling(handling_ship, handling_bullet)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        event_handling.processing_events()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(settings.bg_color)

        # Обновление положения космического корабля и вывод его на экран
        ship.update()
        ship.draw()

        # Обновление, удаление, вывод на экран пуль выпущенных космическим кораблем
        group_bullet.update()
        group_bullet.remove()
        group_bullet.draw()

        # Отображение последнего прорисованного экрана
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
