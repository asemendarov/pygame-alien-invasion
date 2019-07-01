import pygame

from event_handling import CustomEventHandling
from pygame.sprite import Sprite, Group


class Alien(Sprite):
    """ Класс, представляющий одного пришельца """

    def __init__(self, screen, alien_speed_factor=1, fleet_drop_speed=10, fleet_direction=1):
        """ Инициализирует пришельца и задает его начальную позицию """

        super().__init__()

        self.screen = screen

        # Параметры пришельца
        self.alien_speed_factor = alien_speed_factor
        self.fleet_drop_speed = fleet_drop_speed
        self.fleet_direction = fleet_direction  # fleet_direction = 1 обозначает движение вправо; а -1 - влево.

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def update(self):
        """ Обновляет позицию корабля с учетом флага """

        self.x += (self.alien_speed_factor * self.fleet_direction)
        self.rect.x = self.x

    def draw(self):
        """ Выводит пришельца в текущем положении """

        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ Возвращает True, если пришелец находится у края экрана """

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


class GroupAlien:
    """ Группы для хранения пришельцев """

    def __init__(self, group: Group, alien: Alien):
        self.group = group
        self.alien = alien

    def add(self, alien: Alien):
        """ Добавление пришельцев в группу """

        self.group.add(alien or Alien(
            self.alien.screen,
            self.alien.alien_speed_factor,
        ))

    def update(self):
        """ Обновление положения всех пришельцев """

        self._check_fleet_edges()
        self.group.update()

    def remove(self):
        """ Удаление пришельцев """

        pass

    def draw(self):
        """ Вывод на экран пришельцев """

        for alien in self.group.sprites():
            alien.draw()

    def _check_fleet_edges(self):
        """ Реагирует на достижение пришельцем края экрана """

        for alien in self.group.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Опускает весь флот и меняет направление флота """

        for alien in self.group.sprites():
            alien.rect.y += self.alien.fleet_drop_speed
            alien.fleet_direction *= -1


class EventHandlingStandardAlien(CustomEventHandling):
    """ Обработка событий для стандартного пришельца """

    def __init__(self, group_alien: GroupAlien):
        self.group_alien = group_alien

    # Overrides method in CustomEventHandling
    def processing_keydown_events(self, event_key):
        """Обработка событий при зажатии клавиш"""

        if event_key == pygame.K_SPACE:
            pass

    # Overrides method in CustomEventHandling
    def processing_keyup_events(self, event_key):
        """Обработка событий при отпускании клавиш"""

        if event_key == pygame.K_SPACE:
            pass
