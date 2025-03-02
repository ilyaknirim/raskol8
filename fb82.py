import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("8 Круг ада: 2 ров - Льстецы")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Загрузка спрайтов
raskolnikov = pygame.image.load("raskolnikov.png")  # Замените на путь к вашему спрайту
raskolnikov = pygame.transform.scale(raskolnikov, (64, 64))

# Параметры игрока
player_x = screen_width // 2
player_y = screen_height - 100
player_velocity = 0
gravity = 0.5
jump_strength = -10

# Параметры платформ
platform_width, platform_height = 100, 20
platforms = [pygame.Rect(random.randint(0, screen_width - platform_width), random.randint(0, screen_height), platform_width, platform_height)]

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_velocity = jump_strength

    # Обновление позиции игрока
    player_velocity += gravity
    player_y += player_velocity

    # Ограничение движения игрока
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - 64:
        player_y = screen_height - 64

    # Генерация новых платформ
    if len(platforms) < 10:
        platforms.append(pygame.Rect(random.randint(0, screen_width - platform_width), random.randint(0, screen_height), platform_width, platform_height))

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка платформ
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Отрисовка игрока
    screen.blit(raskolnikov, (player_x, player_y))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # Ограничение до 60 кадров в секунду

pygame.quit()