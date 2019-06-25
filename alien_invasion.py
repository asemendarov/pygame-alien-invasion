import pygame

from settings import Settings
from ship import Ship
from event_handling import EventHandling


def run_game(settings):
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    ship = Ship(screen=screen, speed=(1, 1, 1, 1))
    event_handling = EventHandling(ship)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        event_handling.processing_events()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(settings.bg_color)
        ship.update()
        ship.blitme()

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
