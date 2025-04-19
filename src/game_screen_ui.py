
import pygame
import utils
import os
from randomwords import get_random_word
from hangman import Hangman
from gameplay_elements import Gameplay_Elements
from start_screen import StartScreen
from endscreen import EndScreen

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')
screen_color = 'white'
font = os.path.join('resources', 'Roboto-Regular.ttf')
running = True
startscreen = StartScreen(screen)

word = get_random_word()  # Randomly selects a word each time
hangman = Hangman(word)
gameplay_elements = Gameplay_Elements()
print(word)

game_state = 'Start Screen'  # can be Start Screen, Game Screen, or End Screen
game_result = None  # can be win or loss


while running:
    while game_state == 'Start Screen':
        screen.fill('white')
        startscreen.display_all_elements()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startscreen.button_rect.collidepoint(event.pos):
                    game_state = 'Game Screen'
                    break
        pygame.display.flip()

    while game_state == 'Game Screen':
        screen.fill(screen_color)
        hangman.display()
        gameplay_elements.create_underlines(word)
        gameplay_elements.input_answer()
        utils.render_text(gameplay_elements.letter, font, 30, 'black', (370, 400))

        if gameplay_elements.show_invalid_input_message:
            utils.render_text('Invalid input. Only letters allowed', font, 40, 'black', (120, 400))

        # Win condition
        if gameplay_elements.display_correct_guesses(word): #condition that true if all letters have been guessed
            game_result = "win"
            # Reset the game
            word = get_random_word()
            hangman = Hangman(word)
            gameplay_elements = Gameplay_Elements()
            print(word)
            game_state = 'Start Screen'

        # Loss condition
        elif hangman.limb_count >= len(hangman.body_parts):
            game_result = "loss"
            game_state = 'End Screen'

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_state = 'End Screen'
            gameplay_elements.handle_user_input(event, word, gameplay_elements.letter)

        pygame.display.flip()

    while game_state == 'End Screen':
        if game_result == "loss":
            EndScreen.draw_end_screen()
            EndScreen.draw_skulls()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # Reset the game
                word = get_random_word()
                hangman = Hangman(word)
                gameplay_elements = Gameplay_Elements()
                print(word)
                game_state = 'Game Screen'
        pygame.display.flip()