import pygame
from pygame.locals import *

pygame.mixer.init()

sounds = {
        K_a: pygame.mixer.Sound("sounds/a.wav"),
        K_s: pygame.mixer.Sound("sounds/z.wav"),
        K_d: pygame.mixer.Sound("sounds/l.wav"),
        K_f: pygame.mixer.Sound("sounds/g.wav"),
        K_g: pygame.mixer.Sound("sounds/n.wav"),
        K_h: pygame.mixer.Sound("sounds/j.wav"),
        K_j: pygame.mixer.Sound("sounds/c.wav"),
        K_k: pygame.mixer.Sound("sounds/d.wav"),
        K_l: pygame.mixer.Sound("sounds/f.wav"),
        K_z: pygame.mixer.Sound("sounds/s.wav"),
        K_x: pygame.mixer.Sound("sounds/v.wav"),
        K_c: pygame.mixer.Sound("sounds/k.wav"),
        K_v: pygame.mixer.Sound("sounds/x.wav"),
        K_b: pygame.mixer.Sound("sounds/b.wav"),
        K_n: pygame.mixer.Sound("sounds/h.wav"),
        K_m: pygame.mixer.Sound("sounds/m.wav"),
        K_q: pygame.mixer.Sound("sounds/q.wav"),
        K_w: pygame.mixer.Sound("sounds/w.wav"),
        K_e: pygame.mixer.Sound("sounds/e.wav"),
        K_r: pygame.mixer.Sound("sounds/r.wav"),
        K_t: pygame.mixer.Sound("sounds/t.wav"),
        K_y: pygame.mixer.Sound("sounds/y.wav"),
        K_u: pygame.mixer.Sound("sounds/u.wav"),
        K_i: pygame.mixer.Sound("sounds/i.wav"),
        K_o: pygame.mixer.Sound("sounds/o.wav"),
        K_p: pygame.mixer.Sound("sounds/p.wav"),
        K_1: pygame.mixer.Sound("sounds/1.wav"),
        K_2: pygame.mixer.Sound("sounds/2.wav"),
        K_3: pygame.mixer.Sound("sounds/3.wav"),
        K_4: pygame.mixer.Sound("sounds/4.wav"),
        K_5: pygame.mixer.Sound("sounds/5.wav"),
        K_6: pygame.mixer.Sound("sounds/6.wav"),
        K_7: pygame.mixer.Sound("sounds/7.wav"),
        K_8: pygame.mixer.Sound("sounds/8.wav"),
        K_9: pygame.mixer.Sound("sounds/9.wav"),
        K_0: pygame.mixer.Sound("sounds/0.wav"),
    }

background_frames = [
        pygame.image.load("paint/pixil-frame-0.png"),
        pygame.image.load("paint/pixil-frame-1.png"),
        pygame.image.load("paint/pixil-frame-2.png"),
]

