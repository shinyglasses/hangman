import pygame
import utils 
import os
from printingrandomwords import get_random_word
from hangman import Hangman
from gameplay_elements import Gameplay_Elements

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')
screen_color = 'white'
font = os.path.join('resources', 'Roboto-Regular.ttf')
running = True

hangman = Hangman('test')
word = get_random_word() #randomly select a word once we got that
gameplay_elements = Gameplay_Elements()
letter = ''
invalid_answer = False
exceptions = [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_CAPSLOCK]
while running:
    screen.fill(screen_color)
    hangman.display()
    gameplay_elements.create_underlines('test')

    gameplay_elements.input_answer()
    utils.render_text(letter, font, 30, 'black  ', (370, 350))
    if invalid_answer:
        utils.render_text('Invalid input. Only letters allowed', font, 40, 'black', (120, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #checks if mouse is over the answer rect and if user inputs text
        if gameplay_elements.answer_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.KEYDOWN: 
            user_input = pygame.key.name(event.key)
            # checks if its a letter of the alphabet
            if (('a' <= user_input <= 'z') or ('A' <= user_input <= 'Z')) and len(user_input) == 1:
                letter = user_input
                invalid_answer = False
            #removes letter if user presses backspace
            elif event.key == pygame.K_BACKSPACE:
                letter = ''
            elif event.key in exceptions:
                invalid_answer = False
            elif event.key == pygame.K_RETURN:
                pass
               #TO DO: increase limb count if answer is wrong, else put correct letters in corresponding spot
            else:
                letter = ''
                invalid_answer = True
            
            
        
        if event.type == pygame.KEYDOWN: # for testing, remove later
            if event.key == pygame.K_a:  
                hangman.limb_count += 1 
    

    pygame.display.flip()

class Start_Screen:
    pass


