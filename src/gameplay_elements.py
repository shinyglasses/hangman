import pygame
import utils
pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Gameplay_Elements:
    def __init__(self):
        self.answer_rect = self.input_answer()
        # The attributes are here because if they were local variables, it would reset 
        # the variable values back to default each frame
        self.letter = ''
        self.show_invalid_input_message = False
        self.correct_letter = False
        self.underline_coords = [] 
        # The below list is filled with tuples (first value = letter, second value = its position in the word)
        self.correct_letter_and_position_list = []
        self.pending_guess = []
        self.number_of_correct_guesses = 0

    def create_underlines(self, word):
        spacing = 30  # Horizontal space between each underline
        line_length = 40
        first_starting_x = 200  # Starting x position for the first underline
        y_value = 200 
        line_height = 20 
       
        # x_end for the first underline
        x_end = first_starting_x + line_length
    
        # Creates an underline for each letter
        for i in range(len(word)):
            if i == 0:
                x_start = first_starting_x  
            else:
                x_start = x_end + spacing
            
            x_end = x_start + line_length  
            pygame.draw.line(screen, 'black', (x_start, y_value), (x_end, y_value), line_height)
            self.underline_coords.append([x_start, x_end, y_value])
        
    def input_answer(self):
        from game_screen_ui import font  # Imported here to avoid circular imports
        text_rect = utils.render_text('Put desired guess in the box below', font, 40, 'black', (100, 300))
        # Next 2 lines are used to center the rect
        text_rect = text_rect.get_rect() 
        rect_x = 100 + (text_rect.width - 100) // 2
        answer_rect = pygame.Rect(rect_x, 400, 120, 50)  # Lowered and widened the box
        
        # Create a rounded rectangle with a border
        pygame.draw.rect(screen, 'gray', answer_rect, border_radius=10)  # Border radius for rounded corners
        pygame.draw.rect(screen, 'black', answer_rect, 3)  # Black outline (3px thick)
        
        return answer_rect
    
    def check_if_correct_letter(self, word, user_letter):
        matched_positions = []

        if user_letter == '':
            return matched_positions
        self.correct_letter = False
        for position, letter in enumerate(word):
            if user_letter == letter:
                matched_positions.append(position)
                self.correct_letter = True
        return matched_positions

    def handle_user_input(self, event, word, user_letter):
        from game_screen_ui import hangman
        # Checks if mouse is over the answer rect and if user inputs text
        if self.answer_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.KEYDOWN: 
            user_input = pygame.key.name(event.key)
            # Checks if it's a letter of the alphabet
            if (('a' <= user_input <= 'z') or ('A' <= user_input <= 'Z')) and len(user_input) == 1:
                self.letter = user_input
                self.show_invalid_input_message = False
            # Removes letter if user presses backspace
            elif event.key == pygame.K_BACKSPACE:
                self.letter = ''
        
            elif event.key == pygame.K_RETURN:
             
                if self.letter == '':
                # This is here so limbs aren't added if user clicks enter while their cursor is over an empty input box
                    return
                
                positions = self.check_if_correct_letter(word, user_letter)

                if self.correct_letter:
                    for pos in positions:
                        guess = (user_letter, pos)
                        if guess not in self.correct_letter_and_position_list:
                            self.correct_letter_and_position_list.append(guess)
                    self.correct_letter = False
                else:
                    hangman.limb_count += 1
            
            elif pygame.K_1 <= event.key <= pygame.K_9:
                self.show_invalid_input_message = True

    def display_correct_guesses(self, word):
        from game_screen_ui import font
        self.number_of_correct_guesses = 0  # Reset the count each frame

        for letter, position in self.correct_letter_and_position_list:
            x_start, x_end, y_value = self.underline_coords[position]
            utils.render_text(letter, font, 30, 'black', (
                (x_start + x_end) // 2,
                y_value - 30
            ), center=True)
            self.number_of_correct_guesses += 1

        # Return True if all letters have been guessed
        return self.number_of_correct_guesses == len(word)
