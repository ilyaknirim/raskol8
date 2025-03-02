import pygame
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Раскольников и Старушка-процентщица")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Загрузка спрайтов
raskolnikov = pygame.image.load("raskolnikov.png")  # Замените на путь к вашему спрайту
old_woman = pygame.image.load("old_woman.png")     # Замените на путь к вашему спрайту

# Масштабирование спрайтов до 64x64
raskolnikov = pygame.transform.scale(raskolnikov, (64, 64))
old_woman = pygame.transform.scale(old_woman, (64, 64))

# Позиции и углы для кружения
angle_raskolnikov = 0
angle_old_woman = 180
radius = 200  # Радиус кружения
center_x, center_y = screen_width // 2, screen_height // 2  # Центр экрана

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Обновление углов
    angle_raskolnikov += 1
    angle_old_woman -= 1

    # Вычисление позиций для кружения
    raskolnikov_x = center_x + radius * math.cos(math.radians(angle_raskolnikov))
    raskolnikov_y = center_y + radius * math.sin(math.radians(angle_raskolnikov))

    old_woman_x = center_x + radius * math.cos(math.radians(angle_old_woman))
    old_woman_y = center_y + radius * math.sin(math.radians(angle_old_woman))

    # Отрисовка спрайтов
    screen.blit(raskolnikov, (raskolnikov_x - 32, raskolnikov_y - 32))  # Центрирование спрайта
    screen.blit(old_woman, (old_woman_x - 32, old_woman_y - 32))        # Центрирование спрайта

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # Ограничение до 60 кадров в секунду

pygame.quit()

'''git remote add origin https://github.com/ilyaknirim/raskol8.git
git branch -M main
git push -u origin main'''