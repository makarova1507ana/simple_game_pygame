import pygame, sys
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

# Установка размера окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Установка заголовка окна
pygame.display.set_caption('Игра Кликер')

# Определение цветов
NEON_BLUE = (173, 216, 230)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Создание объекта Clock для управления FPS
clock = pygame.time.Clock()
FPS = 30

# Шрифт для отображения счёта
font = pygame.font.SysFont(None, 36)

# Класс для шариков
class Ball:
    def __init__(self, x, y, radius, color, lifetime):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.lifetime = lifetime  # Время жизни шарика в кадрах

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.lifetime -= 1  # Уменьшаем время жизни шарика
        return self.lifetime <= 0  # Возвращаем True если шарик должен исчезнуть

# Переменные для управления шариками
balls = []
ball_spawn_time = 30  # Время между появлениями новых шариков в кадрах
ball_timer = 0

score = 0  # Счётчик очков

def draw_score(surface, score):
    score_text = font.render(f'Score: {score}', True, BLACK)
    surface.blit(score_text, (10, 10))

#-------------------------------Игровой цикл-------------------------------------#
while True:
    # Заполнение окна нежно синим цветом
    window.fill(NEON_BLUE)

    # Обработка событий pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for ball in balls[:]:  # Проходим по копии списка шариков
                if (mouse_x - ball.x) ** 2 + (mouse_y - ball.y) ** 2 <= ball.radius ** 2:
                    balls.remove(ball)
                    score += 1

    # Обновление состояния шариков
    for ball in balls[:]:  # Проходим по копии списка шариков
        if ball.update():
            balls.remove(ball)
        else:
            ball.draw(window)

    # Логика появления новых шариков
    ball_timer += 1
    if ball_timer >= ball_spawn_time:
        ball_timer = 0
        new_ball = Ball(
            x=random.randint(20, WINDOW_WIDTH - 20),
            y=random.randint(20, WINDOW_HEIGHT - 20),
            radius=random.randint(10, 30),
            color=RED,
            lifetime=random.randint(60, 120)  # Время жизни от 2 до 4 секунд при 30 FPS
        )
        balls.append(new_ball)

    # Рисуем счёт
    draw_score(window, score)

    # Ограничение FPS
    clock.tick(FPS)

    pygame.display.update()
#-------------------------------Игровой цикл-------------------------------------#
