import sys
import pygame

from settings import Settings
from ship import Ship


def run_game(settings):
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    ship = Ship(screen)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = False

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
