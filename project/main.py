import pygame
from pygame.locals import *
import pygame_menu
from menu import start_game, quit_game, instr_game


pygame.init()
window = pygame.display.set_mode((700, 450))
pygame.display.set_caption("Виртуальное пианино")

menu = pygame_menu.Menu('Главное меню', 500, 250)
menu.add.button('Играть', start_game)
menu.add.button('Инструкция', instr_game)
menu.add.button('Выход', quit_game)

# Основной цикл приложения
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()

    window.fill((0, 0, 0))
    menu.mainloop(window)
    # Обновление экрана
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()