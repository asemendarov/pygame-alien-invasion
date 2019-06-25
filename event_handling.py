import sys
import pygame


class CustomEventHandling:
    """Пользовательская обработка событий"""

    def processing_keydown_events(self, event_key):
        """Обработка событий при зажатии клавиш"""
        pass

    def processing_keyup_events(self, event_key):
        """Обработка событий при отпускании клавиш"""
        pass


class EventHandling:
    """Обработчик событий"""

    def __init__(self, handler: CustomEventHandling):
        """Инициализация обработчика событий"""

        self.handler = handler

    def processing_events(self):
        """Обработка всех событий"""

        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._processing_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._processing_keyup_events(event)

    def _processing_keydown_events(self, event):
        """Обработка событий при зажатии клавиш"""

        if event.key == pygame.K_ESCAPE:
            sys.exit()
        else:
            self.handler.processing_keydown_events(event.key)

    def _processing_keyup_events(self, event):
        """Обработка событий при отпускании клавиш"""

        self.handler.processing_keyup_events(event.key)


