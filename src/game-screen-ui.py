import pygame
import utils 
import os
from hangman import Hangman
from underline import create_underlines

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')
screen_color = 'white'
font = os.path.join('resources', 'Roboto-Regular.ttf')
running = True

hangman = Hangman('test')
word = 'test' #randomly select a word once we got that

while running:
    screen.fill(screen_color)
    hangman.display()
    create_underlines(word)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  
                hangman.limb_count += 1 
    

    pygame.display.flip()

class Start_Screen:
    pass


