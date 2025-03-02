import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("8 Круг ада: Первый ров")

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Загрузка спрайтов
raskolnikov = pygame.image.load("raskolnikov.png")  # Замените на путь к вашему спрайту
raskolnikov = pygame.transform.scale(raskolnikov, (64, 64))

# Параметры игрока
player_x = 100
player_y = screen_height // 2
player_velocity = 0
gravity = 0.5
jump_strength = -10

# Параметры препятствий
obstacle_width = 100
obstacle_gap = 200
obstacle_velocity = 5
obstacles = []

# Создание препятствий
def create_obstacle():
    gap_y = random.randint(100, screen_height - 100 - obstacle_gap)
    top_obstacle_height = gap_y
    bottom_obstacle_y = gap_y + obstacle_gap
    obstacles.append(pygame.Rect(screen_width, 0, obstacle_width, top_obstacle_height))
    obstacles.append(pygame.Rect(screen_width, bottom_obstacle_y, obstacle_width, screen_height - bottom_obstacle_y))

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

    # Создание новых препятствий
    if len(obstacles) == 0 or obstacles[-1].x < screen_width - 300:
        create_obstacle()

    # Движение препятствий
    for obstacle in obstacles:
        obstacle.x -= obstacle_velocity

    # Удаление препятствий за пределами экрана
    if len(obstacles) > 0 and obstacles[0].x < -obstacle_width:
        obstacles.pop(0)
        obstacles.pop(0)

    # Проверка коллизий
    player_rect = pygame.Rect(player_x, player_y, 64, 64)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            print("Игра окончена!")
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка препятствий
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # Отрисовка игрока
    screen.blit(raskolnikov, (player_x, player_y))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # Ограничение до 60 кадров в секунду

pygame.quit()
sys.exit()