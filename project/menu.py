import pygame
from pygame.locals import *
from key_and_back import sounds, background_frames

pygame.init()
window = pygame.display.set_mode((700, 450))


def quit_game():
    pygame.quit()
    quit()


def start_game():

    character_frames = []
    character_frames.append(pygame.image.load("paint/man1.png").convert_alpha())
    character_frames.append(pygame.image.load("paint/man2.png").convert_alpha())
    character_frames.append(pygame.image.load("paint/man3.png").convert_alpha())
    character_frames.append(pygame.image.load("paint/man4.png").convert_alpha())
    character_frames.append(pygame.image.load("paint/man5.png").convert_alpha())
    character_frames.append(pygame.image.load("paint/man6.png").convert_alpha())
    cat = []
    cat.append(pygame.image.load("paint/cat0.png").convert_alpha())
    cat.append(pygame.image.load("paint/cat1.png").convert_alpha())
    cat.append(pygame.image.load("paint/cat2.png").convert_alpha())
    cat.append(pygame.image.load("paint/cat3.png").convert_alpha())
    cat.append(pygame.image.load("paint/cat4.png").convert_alpha())
    cat.append(pygame.image.load("paint/cat5.png").convert_alpha())
    current_frame = 0
    cats_frame = 0
    frame_delay = 70
    character_x = 155
    character_y = 215
    cat_x = 455
    cat_y = 220

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Если нажата клавиша
                if event.key in sounds:
                    # Проигрывание соответствующего звука
                    sounds[event.key].play()
                elif event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False

            # Обновление фона
            current_frame += 1
            cats_frame += 1
            if current_frame >= len(background_frames):
                current_frame = 0
                cats_frame = 0

            # Отрисовка фона
            window.blit(background_frames[current_frame], (0, 0))
            window.blit(character_frames[current_frame], (character_x, character_y))
            window.blit(cat[cats_frame], (cat_x, cat_y))

        # Обновление экрана
        pygame.display.flip()
        pygame.time.delay(frame_delay)


def instr_game():
    window = pygame.display.set_mode((700, 450))
    back_img = pygame.image.load("paint/instr.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False

        window.blit(back_img, (0, 0))

        pygame.display.flip()

