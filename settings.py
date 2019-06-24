class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self, title, size=None, color=None):
        """Инициализирует настройки игры."""

        # Параметры экрана
        self.title = title
        self.screen_width, self.screen_height = size or (1200, 800)
        self.bg_color = color or (230, 230, 230)