import pygame
import utils

pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Gameplay_Elements:
    def __init__(self):
        self.answer_rect = self.input_answer()
        #the attributes are here because if they were local variables, it would reset 
        #the variables values back to default each frame
        self.letter = ''
        self.show_invalid_input_message = False
        self.correct_letter = False
        self.underline_coords = [] 
        #the below list is filled with tuples(first value = letter, second value = its position in the word)
        self.correct_letter_and_position_list = []
        self.pending_guess = []
        self.number_of_correct_guesses = 0

    def create_underlines(self, word):
        spacing = 30  #horizontal space between each underline
        line_length = 40
        first_starting_x = 200  #starting x position for the first underline
        y_value = 200 
        line_height = 20 
       
        #x_end for the first underline
        x_end = first_starting_x + line_length
    
        #creates an underline for each letter
        for i in range(len(word)):
            if i == 0:
                x_start = first_starting_x  
            else:
                x_start = x_end + spacing
            
            x_end = x_start + line_length  
            pygame.draw.line(screen, 'black', (x_start, y_value), (x_end, y_value), line_height)
            self.underline_coords.append([x_start, x_end, y_value])
        
    def input_answer(self):
        from game_screen_ui import font #imported here to avoid circular imports
        text_rect = utils.render_text('Put desired guess in the box below', font, 40, 'black', (100, 300))
        #next 2 lines are used to center the rect
        text_rect = text_rect.get_rect() 
        rect_x = 100 + (text_rect.width - 100)//2
        answer_rect = pygame.draw.rect(screen, 'gray', pygame.Rect(rect_x, 350, 100, 50))
        return  answer_rect
    
    def check_if_correct_letter(self, word, user_letter):
        matched_positions = []

        if user_letter == '':
            return matched_positions
        self.correct_letter = False
        for position, letter in enumerate(word):
            #TO DO: the appending to pending guesses needs to change
                if user_letter == letter:
                  matched_positions.append(position)
                  self.correct_letter = True
        return matched_positions

                
    def handle_user_input(self, event, word, user_letter):
        from game_screen_ui import hangman
        #exceptions are so it doesnt show something non letters, like "shift", in the input box 
        exceptions = [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_CAPSLOCK, pygame.K_RMETA, pygame.K_LMETA,
                      pygame.K_MINUS, pygame.K_EQUALS, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET, pygame.K_SPACE,
                      pygame.K_SEMICOLON, pygame.K_QUOTE, pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH]
        #checks if mouse is over the answer rect and if user inputs text
        if self.answer_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.KEYDOWN: 
            user_input = pygame.key.name(event.key)
            # checks if its a letter of the alphabet
            if (('a' <= user_input <= 'z') or ('A' <= user_input <= 'Z')) and len(user_input) == 1:
                self.letter = user_input
                self.show_invalid_input_message = False
            #removes letter if user presses backspace
            elif event.key == pygame.K_BACKSPACE:
                self.letter = ''
            elif event.key in exceptions:
                 #here so it doesnt show non letters in the box (if putting numbers, itll say invalid input)
                pass
            
            elif event.key == pygame.K_RETURN:
                if not self.letter:
                   pass  #dont do anything for entering on an empty input box

                positions = self.check_if_correct_letter(word, user_letter)

                if self.correct_letter:
                    for pos in positions:
                        guess = (user_letter, pos)
                        if guess not in self.correct_letter_and_position_list:
                            self.correct_letter_and_position_list.append(guess)
                    self.correct_letter = False
                else:
                    hangman.limb_count += 1
            
            elif self.letter == '':
                #this is here so limbs arent added if user clicks enter while their cursor is over an empty input box
                pass
                
            else:
                self.show_invalid_input_message = True

    def display_correct_guesses(self, word):
        from game_screen_ui import font
        for letter, position in self.correct_letter_and_position_list:
            x_start, x_end, y_value = self.underline_coords[position]
            utils.render_text(letter, font, 30, 'black', (
                (x_start + x_end) // 2,
                y_value - 40
            ))  
            self.number_of_correct_guesses += 1
            if self.number_of_correct_guesses == len(word):
                #nelson, add win screen here
                pass