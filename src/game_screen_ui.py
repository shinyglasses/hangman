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
letter = gameplay_elements.letter
invalid_answer = gameplay_elements.invalid_answer


while running:
    screen.fill(screen_color)
    hangman.display()
    gameplay_elements.create_underlines(word)

    gameplay_elements.input_answer()

    utils.render_text(gameplay_elements.letter, font, 30, 'black', (370, 350))
    print(letter)
    gameplay_elements.check_if_correct_letter(word, gameplay_elements.letter)
    if invalid_answer:
        utils.render_text('Invalid input. Only letters allowed', font, 40, 'black', (120, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        gameplay_elements.handle_user_input(event)
        
        if event.type == pygame.KEYDOWN: # for testing, remove later
            if event.key == pygame.K_a:  
                hangman.limb_count += 1 
    

    pygame.display.flip()