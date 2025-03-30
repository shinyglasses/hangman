import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))


def create_underlines(word):
    spacing = 20 #the space between each underline 
    underline_count = 0 #number of underlines drawn
    for letter in len(word):
        underline_count += 1
        pygame.draw_line(screen, 'black', (200, 200), (200, 230), 20)
        