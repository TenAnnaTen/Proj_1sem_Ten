import pygame
from pygame.locals import *
from key_and_back import load_sounds, load_background_frames, character_frames, cat


pygame.init()
window = pygame.display.set_mode((700, 450))


def quit_game():
    pygame.quit()
    quit()


def start_game():
    sounds = load_sounds()
    background_frames = load_background_frames()
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
                if event.key in sounds:
                    sounds[event.key].play()
                elif event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False

        current_frame += 1
        cats_frame += 1
        if current_frame >= len(background_frames):
            current_frame = 0
            cats_frame = 0

        window.blit(background_frames[current_frame], (0, 0))
        window.blit(character_frames[current_frame], (character_x, character_y))
        window.blit(cat[cats_frame], (cat_x, cat_y))

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
