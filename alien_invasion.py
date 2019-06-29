import pygame

from pygame.sprite import Group

from ship import Ship, EventHandlingStandardShip
from bullet import Bullet, GroupBullet, EventHandlingStandardBullet
from alien import Alien, GroupAlien, EventHandlingStandardAlien
from settings import Settings
from event_handling import EventHandling


def get_number_aliens_x(alien_width):
    """ Вычисляет количество пришельцев в ряду """

    available_space_x = Settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ship_height, alien_height):
    """ Определяет количество рядов, помещающихся на экране """

    available_space_y = (Settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(screen, group_alien, alien_number, row_number):
    """ Создает пришельца и размещает его в ряду """

    alien = Alien(screen=screen, alien_speed_factor=group_alien.alien.alien_speed_factor)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    group_alien.add(alien)


def create_fleet(screen, group_alien, ship):
    """ Создает флот пришельцев """

    # Создание пришельца и вычисление количества пришельцев в ряду
    number_aliens_x = get_number_aliens_x(group_alien.alien.rect.width)
    number_rows = get_number_rows(ship.rect.height, group_alien.alien.rect.height)

    # Создание первого ряда пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(screen, group_alien, alien_number, row_number)


def run_game():
    screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
    pygame.display.set_caption(Settings.title)

    # Создание космического корабля, пришельца и пули
    ship = Ship(screen=screen, speed_ship=(2, 2, 2, 2))
    bullet = Bullet(screen=screen, ship=ship, bullet_speed_factor=1,
                    bullet_width=3, bullet_height=15, bullet_color=(60, 60, 60))
    alien = Alien(screen=screen, alien_speed_factor=1)

    # Создание группы для хранения пуль и группы для хранения пришельцев
    group_bullet = GroupBullet(Group(), bullet)
    group_alien = GroupAlien(Group(), alien)

    # Создание обработчика для космического корабля и пуль
    handling_ship = EventHandlingStandardShip(ship)
    handling_bullet = EventHandlingStandardBullet(group_bullet)
    handling_alien = EventHandlingStandardAlien(group_alien)
    event_handling = EventHandling(handling_ship, handling_bullet, handling_alien)

    create_fleet(screen, group_alien, ship)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        event_handling.processing_events()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(Settings.bg_color)

        # Обновление положения космического корабля и вывод его на экран
        ship.update()
        ship.draw()

        # Обновление, удаление, вывод на экран пуль выпущенных космическим кораблем
        group_bullet.update()
        group_bullet.remove()
        group_bullet.draw()

        # Обновление, удаление, вывод на экран пришельцев
        group_alien.update()
        group_alien.remove()
        group_alien.draw()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


def main():
    # Инициируем игру и создаем объект экрана
    pygame.init()

    # Запускаем игру
    run_game()


if __name__ == '__main__':
    main()
