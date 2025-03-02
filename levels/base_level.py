import pygame

class Level:
    def __init__(self, screen):
        """
        Базовый класс для всех уровней.
        
        :param screen: Экран Pygame, на котором будет отрисовываться уровень.
        """
        self.screen = screen
        self.complete = False  # Флаг завершения уровня

    def run(self):
        """
        Основной метод для запуска уровня.
        Должен быть переопределен в каждом подклассе.
        """
        raise NotImplementedError("Метод run должен быть переопределен в подклассе")

    def is_complete(self):
        """
        Проверяет, завершен ли уровень.
        
        :return: True, если уровень завершен, иначе False.
        """
        return self.complete