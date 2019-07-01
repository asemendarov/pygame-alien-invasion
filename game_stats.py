from settings import Settings

class GameStats():
    """ Отслеживание статистики для игры Alien Invasion """

    def __init__(self):
        """ Инициализирует статистику """

        # Игра Alien Invasion запускается в активном состоянии
        self.game_active = True

        self.reset_stats()

    def reset_stats(self):
        """ Инициализирует статистику, изменяющуюся в ходе игры """

        self.ships_left = Settings.ship_limit
