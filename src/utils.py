
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

def render_text(text, font, font_size, color, position, center=False):
    font = pygame.font.Font(font, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    if center:
        text_rect.center = position
    else:
        text_rect.topleft = position

    screen.blit(text_surface, text_rect)
    return text_surface