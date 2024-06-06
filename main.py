import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Кликер с шариками')

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Шрифт
font = pygame.font.SysFont("monospace", 50)

# Параметры игры
score = 0
balls = []
ball_size = 30
ball_spawn_time = 2000  # Время в миллисекундах между появлениями новых шариков
ball_life_time = 3000  # Время в миллисекундах, через которое шарик исчезает

# Настройка времени
last_spawn_time = pygame.time.get_ticks()

# Основной игровой цикл
running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for ball in balls[:]:
                ball_rect = pygame.Rect(ball['pos'][0] - ball_size // 2, ball['pos'][1] - ball_size // 2, ball_size, ball_size)
                if ball_rect.collidepoint(mouse_pos):
                    balls.remove(ball)
                    score += 1

    # Появление новых шариков
    if current_time - last_spawn_time > ball_spawn_time:
        ball_pos = [random.randint(0, width), random.randint(0, height)]
        balls.append({'pos': ball_pos, 'spawn_time': current_time})
        last_spawn_time = current_time

    # Удаление старых шариков
    for ball in balls[:]:
        if current_time - ball['spawn_time'] > ball_life_time:
            balls.remove(ball)

    # Отрисовка объектов
    window.fill(black)
    for ball in balls:
        pygame.draw.circle(window, red, ball['pos'], ball_size)

    # Отображение счета
    score_text = font.render(f"Счет: {score}", True, white)
    window.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
