
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

def render_text(text, font, font_size, color, position):
    font = pygame.font.Font(font, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
    return text_surface
