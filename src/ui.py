import pygame
import utils 
import os

print("Current working directory:", os.getcwd())

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')

font = os.path.join('resources', 'Roboto-Regular.ttf')

running = True

while running:

    utils.render_text('Welcome to Hangman!',font, 98, 'purple', (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

class Start_Screen:
    pass


    