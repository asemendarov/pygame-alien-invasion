import pygame

from pygame.sprite import Sprite, Group
from event_handling import CustomEventHandling


class Bullet(Sprite):
    """ Класс описывающий состояние и поведение пуль выпущенных космическим кораблем """

    def __init__(self, screen, ship, bullet_speed_factor=1, bullet_width=3,
                 bullet_height=15, bullet_color=(60, 60, 60)):

        super().__init__()

        self.screen = screen
        self.ship = ship

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
        """ Перемещает пулю вверх по экрану """

        # Обновление позиции пули в вещественном формате
        self.y -= self.bullet_speed_factor

        # Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw(self):
        """ Вывод пули на экран """

        pygame.draw.rect(self.screen, self.bullet_color, self.rect)


class GroupBullet:
    """ Группы для хранения пуль """

    def __init__(self, group: Group, bullet: Bullet):
        self.group = group
        self.bullet = bullet

    def add(self):
        """ Добавление пули в группу """

        self.group.add(Bullet(
            self.bullet.screen, self.bullet.ship, self.bullet.bullet_speed_factor,
            self.bullet.bullet_width, self.bullet.bullet_height, self.bullet.bullet_color
        ))

    def update(self):
        """ Обновление положения всех пуль выпущенных космическим кораблем """

        self.group.update()

    def remove(self):
        """ Удаление пуль, вышедших за край экрана по оси Y """

        for bullet in self.group.copy():
            if bullet.rect.bottom <= 0:
                self.group.remove(bullet)

    def draw(self):
        """ Вывод на экран всех пуль выпущенных космическим кораблем """

        for bullet in self.group.sprites():
            bullet.draw()


class EventHandlingStandardBullet(CustomEventHandling):
    """ Обработка событий для стандартной пули """

    def __init__(self, group_bullet: GroupBullet):
        self.group_bullet = group_bullet

    # Overrides method in CustomEventHandling
    def processing_keydown_events(self, event_key):
        """Обработка событий при зажатии клавиш"""

        if event_key == pygame.K_SPACE:
            self.group_bullet.add()

    # Overrides method in CustomEventHandling
    def processing_keyup_events(self, event_key):
        """Обработка событий при отпускании клавиш"""

        if event_key == pygame.K_SPACE:
            pass
