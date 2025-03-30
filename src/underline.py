import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

#there has to be a limit to how many letters a word can have b/c otherwise the underlines wont fit in the screen
def create_underlines(word):
    spacing = 30  # horizontal space between each underline
    line_length = 40
    first_starting_x = 200  # starting x position for the first underline
    y_value = 200 
    line_height = 20 

    # x_end for the first underline
    x_end = first_starting_x + line_length
    
    #creates an underline for each letter
    for i in range(len(word)):
        if i == 0:
            x_start = first_starting_x  
        else:
            x_start = x_end + spacing
        
        x_end = x_start + line_length  
        
        pygame.draw.line(screen, 'black', (x_start, y_value), (x_end, y_value), line_height)
