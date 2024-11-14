import pygame
import random

# Инициализация Pygame
pygame.init()

pygame.mixer.init()

# Загрузка музыки и воспроизведение в цикле
pygame.mixer.music.load("music/last.mp3")
pygame.mixer.music.play(-1, 0.0)

# Размеры окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя игра Bir Balee")
icon = pygame.image.load("img/tornado.png")
pygame.display.set_icon(icon)

# Класс снежинки
class Snowflake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))  # Размер снежинки
        self.image.fill((255, 255, 255))  # Белый цвет
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)  # Начальная позиция по X
        self.rect.y = random.randint(-20, 600)  # Начальная позиция по Y (сверху)
        self.speed = random.randint(1, 3)  # Случайная скорость падения

    def update(self):
        # Двигаем снежинку вниз
        self.rect.y += self.speed
        
        # Если снежинка вышла за пределы экрана, перемещаем её на верхний край
        if self.rect.y > 600:
            self.rect.y = random.randint(-20, -5)
            self.rect.x = random.randint(0, 800)

# Группа для всех снежинок
snowflakes = pygame.sprite.Group()

# Создаем снежинки
for _ in range(100):
    snowflake = Snowflake()
    snowflakes.add(snowflake)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Завершаем игру, если окно закрыто

    # Отображение фона (небо)
    screen.fill((93, 130, 243))  # Цвет неба (голубой)

    # Рисуем тело снеговика
    pygame.draw.circle(screen, (255, 255, 255), (400, 500), 90)
    pygame.draw.circle(screen, (255, 255, 255), (400, 400), 70)
    pygame.draw.circle(screen, (255, 255, 255), (400, 300), 50)
    
    # Пуговицы снеговика
    pygame.draw.circle(screen, (0, 0, 0), (400, 500), 5)
    pygame.draw.circle(screen, (0, 0, 0), (400, 400), 5)
    
    # Глаза снеговика
    pygame.draw.circle(screen, (0, 0, 0), (380, 290), 5)
    pygame.draw.circle(screen, (0, 0, 0), (420, 290), 5)

    # Руки снеговика
    pygame.draw.line(screen, (109, 79, 18), (470, 390), (550, 400), 5)
    pygame.draw.line(screen, (109, 79, 18), (250, 400), (330, 390), 5)
    
    # Нос снеговика
    pygame.draw.polygon(screen, (196, 141, 30), ((400, 300), (400, 320), (450, 310)))
    
    # Рот снеговика
    pygame.draw.line(screen, (109, 79, 18), (385, 325), (415, 325), 3)

    # Рисуем облако
    pygame.draw.circle(screen, (200, 200, 200), (50, 50), 70)
    pygame.draw.circle(screen, (200, 200, 200), (130, 30), 50)
    pygame.draw.circle(screen, (200, 200, 200), (212, 40), 59)
    pygame.draw.circle(screen, (200, 200, 200), (300, 47), 67)
    pygame.draw.circle(screen, (200, 200, 200), (385, 30), 50)
    pygame.draw.circle(screen, (200, 200, 200), (450, 20), 40)
    pygame.draw.circle(screen, (200, 200, 200), (750, 50), 70)
    pygame.draw.circle(screen, (200, 200, 200), (655, 47), 67)
    pygame.draw.circle(screen, (200, 200, 200), (575, 20), 40)

    # Земля
    pygame.draw.line(screen, (255, 255, 255), (0, 595), (800, 595), 50)

    # Обновление снежинок
    snowflakes.update()

    # Отображаем снежинки
    snowflakes.draw(screen)

    # Обновляем экран
    pygame.display.flip()

    # Ограничение частоты кадров (60 кадров в секунду)
    pygame.time.Clock().tick(60)

# Завершение работы Pygame
pygame.mixer.music.stop()  # Остановка музыки при выходе

for event in pygame.event.get():
    if event.type == pygame.QUIT():
 
        pygame.quit()
 
        exit()