import pygame
import random
from levels.base_level import Level

class Level8_1(Level):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen_width, self.screen_height = screen.get_size()
        self.player = pygame.Rect(100, self.screen_height // 2, 64, 64)
        self.obstacles = []
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.velocity = self.jump_strength

            # Обновление позиции игрока
            self.velocity += self.gravity
            self.player.y += self.velocity

            # Генерация препятствий
            if len(self.obstacles) == 0 or self.obstacles[-1].x < self.screen_width - 300:
                self.create_obstacle()

            # Движение препятствий
            for obstacle in self.obstacles:
                obstacle.x -= 5

            # Удаление препятствий за пределами экрана
            if len(self.obstacles) > 0 and self.obstacles[0].x < -100:
                self.obstacles.pop(0)

            # Проверка коллизий
            for obstacle in self.obstacles:
                if self.player.colliderect(obstacle):
                    running = False

            # Очистка экрана
            self.screen.fill((0, 0, 0))

            # Отрисовка препятствий
            for obstacle in self.obstacles:
                pygame.draw.rect(self.screen, (255, 0, 0), obstacle)

            # Отрисовка игрока
            pygame.draw.rect(self.screen, (0, 0, 255), self.player)

            # Обновление экрана
            pygame.display.flip()
            clock.tick(60)

    def create_obstacle(self):
        gap_y = random.randint(100, self.screen_height - 100 - 200)
        top_obstacle = pygame.Rect(self.screen_width, 0, 100, gap_y)
        bottom_obstacle = pygame.Rect(self.screen_width, gap_y + 200, 100, self.screen_height - gap_y - 200)
        self.obstacles.append(top_obstacle)
        self.obstacles.append(bottom_obstacle)