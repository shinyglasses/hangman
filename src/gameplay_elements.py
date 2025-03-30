import pygame
import utils

pygame.init()
screen = pygame.display.set_mode((1280, 720))

#there has to be a limit to how many letters a word can have b/c otherwise the underlines wont fit in the screen
class Gameplay_Elements:
    def __init__(self):
        self.answer_rect = self.input_answer()
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

    def input_answer(self):
        from game_screen_ui import font #imported here to avoid circular imports
        text_rect = utils.render_text('Put desired guess in the box below', font, 40, 'black', (100, 300))
        #next 2 lines are used to center the rect
        text_rect = text_rect.get_rect() 
        rect_x = 100 + (text_rect.width - 100)//2
        answer_rect = pygame.draw.rect(screen, 'gray',pygame.Rect(rect_x, 350, 100, 50))
        return  answer_rect
    