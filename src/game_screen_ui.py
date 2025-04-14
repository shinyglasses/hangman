import pygame
import utils 
import os
from randomwords import get_random_word
from hangman import Hangman
from gameplay_elements import Gameplay_Elements

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')
screen_color = 'white'
font = os.path.join('resources', 'Roboto-Regular.ttf')
running = True

word = get_random_word() #randomly selects a word 
hangman = Hangman(word)

gameplay_elements = Gameplay_Elements()

print(word) #TO DO: remove this line (just here for debugging)

while running:
    screen.fill(screen_color)
    hangman.display()
    gameplay_elements.create_underlines(word)

    gameplay_elements.input_answer()

    #displays user letter in the textbox
    utils.render_text(gameplay_elements.letter, font, 30, 'black', (370, 350))

    gameplay_elements.display_correct_guesses(word)
    
    if gameplay_elements.show_invalid_input_message:
        utils.render_text('Invalid input. Only letters allowed', font, 40, 'black', (120, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        gameplay_elements.handle_user_input(event, word, gameplay_elements.letter)
    pygame.display.flip()
