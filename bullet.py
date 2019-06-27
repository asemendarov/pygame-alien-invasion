import pygame
from pygame.sprite import Sprite
from event_handling import CustomEventHandling


class Bullet(Sprite, CustomEventHandling):
    """Класс описывающий состояние и поведение пуль выпускаемых космическим кораблем"""

    def __init__(self, screen, ship, bullets, bullet_speed_factor=1,
                 bullet_width=3, bullet_height=15, bullet_color=(60, 60, 60)):
        super().__init__()

        self.screen = screen
        self.ship = ship
        self.bullets = bullets

        # Параметры пули
        self.bullet_speed_factor = bullet_speed_factor
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.bullet_color = bullet_color

        # Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, bullet_width, bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

    # Overrides method in Sprite
    def update(self):
        """Перемещает пулю вверх по экрану"""

        # Обновление позиции пули в вещественном формате
        self.y -= self.bullet_speed_factor

        # Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран"""

        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

    # Overrides method in CustomEventHandling
    def processing_keydown_events(self, event_key):
        """Обработка событий при зажатии клавиш"""

        if event_key == pygame.K_SPACE:
            self.bullets.add(Bullet(
                self.screen, self.ship, self.bullets, self.bullet_speed_factor,
                self.bullet_width, self.bullet_height, self.bullet_color
            ))

    # Overrides method in CustomEventHandling
    def processing_keyup_events(self, event_key):
        """Обработка событий при отпускании клавиш"""

        if event_key == pygame.K_SPACE:
            pass