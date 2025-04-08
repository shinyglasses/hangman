import pygame
import utils
import os
pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = os.path.join('resources', 'Roboto-Regular.ttf')

class Gameplay_Elements:
    def __init__(self):
        self.answer_rect = self.input_answer()
        #the below attributes are here because if i put them as local variables, it would remain '' 
        #or False the entire time bc handle_user_input is called every frame     
        self.letter = ''
        self.invalid_answer = False
        self.correct_letter = False
        self.underline_coords = []
        self.show_letter = False
        self.correct_letter_list = []
        self.underline_positions = []


    def create_underlines(self, word):
        spacing = 30  #horizontal space between each underline
        line_length = 40
        first_starting_x = 200  #starting x position for the first underline
        y_value = 200 
        line_height = 20 
       
        #x_end for the first underline
        x_end = first_starting_x + line_length
    
        #creates an underline for each letter
        for i in range(len(word) + 1):
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
        answer_rect = pygame.draw.rect(screen, 'gray',pygame.Rect(rect_x, 350, 100, 50))
        return  answer_rect
    
    def check_if_correct_letter(self, word, letter):
        from game_screen_ui import hangman

        correct_letter = False
        if letter == '':
            return
        for i in range(len(word)):
            if letter in word[i]:
                self.underline_positions.append(i)
                self.correct_letter_list.append(letter)
                correct_letter = True
        if not correct_letter:
            hangman.limb_count += 1
            
                
    
    
    def handle_user_input(self, event):
        exceptions = [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_CAPSLOCK]
        #checks if mouse is over the answer rect and if user inputs text
        if self.answer_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.KEYDOWN: 
            user_input = pygame.key.name(event.key)
            # checks if its a letter of the alphabet
            if (('a' <= user_input <= 'z') or ('A' <= user_input <= 'Z')) and len(user_input) == 1:
                self.letter = user_input
                self.correct_letter = True
                self.invalid_answer = False
            #removes letter if user presses backspace
            elif event.key == pygame.K_BACKSPACE:
                self.letter = ''
        
            elif event.key in exceptions:
                pass
            elif event.key == pygame.K_RETURN:
                if self.correct_letter:
                   self.show_letter = True
            else:
                self.invalid_answer = True

    def display_correct_guesses(self, word):
        self.check_if_correct_letter(word, self.letter)
    
        print(self.underline_positions)
        for position in self.underline_positions:
            for letter in self.correct_letter_list:
                x_start, x_end, y_value = self.underline_coords[position]
                utils.render_text(letter, font, 30, 'black', (
                    (x_start + x_end) // 2,
                    y_value - 40
                ))  