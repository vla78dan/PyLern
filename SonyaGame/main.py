import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вкусняшки для Сони")

DARK_BLUE = (10, 17, 149)
WHITE = (245, 245, 245)
GREEN = (63, 255, 0)
RED = (236, 3, 4)
YELLOW = (255, 255, 0)
PINK = (251, 0, 129)

clock = pygame.time.Clock()
running = True

while running:
    current_time = pygame.time.get_ticks()
    dt = clock.tick(60) / 1000

    WIN.fill(DARK_BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()

# DARK_BLUE = (10, 10, 40)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 255, 0)
# PINK = (255, 0, 255)
#
# # ИНИЦИАЛИЗАЦИЯ ИГРЫ
# clock = pygame.time.Clock()  # Для контроля FPS
# running = True  # Флаг работы игры
#
# # ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ
# while running:
#     current_time = pygame.time.get_ticks()
#     dt = clock.tick(60) / 1000
#
#     WIN.fill(DARK_BLUE)
#
#     # Обработка событий
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:  # Если закрыли окно
#             running = False
#
#     pygame.display.update()  # Обновление экрана
#
# pygame.quit()  # Корректный выход
