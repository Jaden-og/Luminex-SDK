import pygame

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return screen

def draw_rectangle(screen, color, rect):
    pygame.draw.rect(screen, color, rect)
