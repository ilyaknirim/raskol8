import pygame
import sys
from levels.level_8_1 import Level8_1
# from levels.level_8_2 import Level8_2
# from levels.level_8_3 import Level8_3
# from levels.level_8_4 import Level8_4
# from levels.level_8_5 import Level8_5
# from levels.level_8_6 import Level8_6
# from levels.level_8_7 import Level8_7
# from levels.level_8_8 import Level8_8
# from levels.level_8_9 import Level8_9
# from levels.level_8_10 import Level8_10

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("8 Круг ада: Путешествие Раскольникова")

# Основной игровой цикл
def main():
    levels = [
        Level8_1(screen),
        # Level8_2(screen),
        # Level8_3(screen),
        # Level8_4(screen),
        # Level8_5(screen),
        # Level8_6(screen),
        # Level8_7(screen),
        # Level8_8(screen),
        # Level8_9(screen),
        # Level8_10(screen)
    ]

    current_level = 0

    while current_level < len(levels):
        level = levels[current_level]
        level.run()

        if level.is_complete():
            current_level += 1
        else:
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()