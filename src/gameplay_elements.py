import pygame
import utils

pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Gameplay_Elements:
    def __init__(self):
        self.answer_rect = self.input_answer()
        #the below attributes are here because if i put them as local variables, it would remain '' 
        #or False the entire time bc handle_user_input is called every frame     
        self.letter = ''
        self.invalid_answer = False

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

    def input_answer(self):
        from game_screen_ui import font #imported here to avoid circular imports
        text_rect = utils.render_text('Put desired guess in the box below', font, 40, 'black', (100, 300))
        #next 2 lines are used to center the rect
        text_rect = text_rect.get_rect() 
        rect_x = 100 + (text_rect.width - 100)//2
        answer_rect = pygame.draw.rect(screen, 'gray',pygame.Rect(rect_x, 350, 100, 50))
        return  answer_rect
    
    def check_if_correct_letter(self, word, letter):
        positions = []
        for i in range(len(word)):
            if letter in word[i]:
             positions.append(i)
        return positions
    
    def handle_user_input(self, event):
        exceptions = [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_CAPSLOCK]
        #checks if mouse is over the answer rect and if user inputs text
        if self.answer_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.KEYDOWN: 
            user_input = pygame.key.name(event.key)
            # checks if its a letter of the alphabet
            if (('a' <= user_input <= 'z') or ('A' <= user_input <= 'Z')) and len(user_input) == 1:
                self.letter = user_input
                self.invalid_answer = False
            #removes letter if user presses backspace
            elif event.key == pygame.K_BACKSPACE:
                self.letter = ''
            elif event.key in exceptions:
                self.letter = 'test'
                self.invalid_answer = False
            elif event.key == pygame.K_RETURN:
                pass
               #TO DO: increase limb count if answer is wrong, else put correct letters in corresponding spot
            else:
                self.invalid_answer = True