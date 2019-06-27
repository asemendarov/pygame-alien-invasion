import pygame
from event_handling import CustomEventHandling


class Ship(CustomEventHandling):
    """Класс описывающий состояние и поведение космического корабля"""

    def __init__(self, screen, speed_ship=(1., 1., 1., 1.)):
        """Инициализирует корабль и задает его начальную позицию"""

        self.screen = screen
        self.speed = speed_ship

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Флаг перемещения
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.speed[3]
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed[1]
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.speed[0]
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed[2]

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Рисует корабль в текущей позиции."""

        self.screen.blit(self.image, self.rect)

    # Overrides method in CustomEventHandling
    def processing_keydown_events(self, event_key):
        """Обработка событий при зажатии клавиш"""

        if event_key == pygame.K_LEFT:
            self.moving_left = True
        elif event_key == pygame.K_RIGHT:
            self.moving_right = True
        elif event_key == pygame.K_UP:
            self.moving_up = True
        elif event_key == pygame.K_DOWN:
            self.moving_down = True

    # Overrides method in CustomEventHandling
    def processing_keyup_events(self, event_key):
        """Обработка событий при отпускании клавиш"""

        if event_key == pygame.K_LEFT:
            self.moving_left = False
        elif event_key == pygame.K_RIGHT:
            self.moving_right = False
        elif event_key == pygame.K_UP:
            self.moving_up = False
        elif event_key == pygame.K_DOWN:
            self.moving_down = False
