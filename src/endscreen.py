""" import pygame
import utils 
import os

print("Current working directory:", os.getcwd())

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')

font = os.path.join('resources', 'Roboto-Regular.ttf')

running = True

class EndScreen:
    def __init__(self, screen, message="You Lost!!", sub_message="Press any key to continue"):
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('resources', 'Roboto-Regular.ttf'), 50)
        self.sub_font = pygame.font.Font(os.path.join('resources', 'Roboto-Regular.ttf'), 30)
        self.message = message
        self.sub_message = sub_message

    def display(self):
        self.screen.fill((255, 255, 255))  # Screen color
        text = self.font.render(self.message, True, (0, 0, 0))  # Main message
        text_rect = text.get_rect(center=(1280 // 2, 720 // 2 - 30))
        self.screen.blit(text, text_rect)
        
        sub_text = self.sub_font.render(self.sub_message, True, (100, 100, 100))  # Sub message
        sub_text_rect = sub_text.get_rect(center=(1280 // 2, 900 // 2 + 30))
        self.screen.blit(sub_text, sub_text_rect)
        
    def anykey(self):
        
        pygame.display.flip()

end_screen = EndScreen(screen)
end_screen.display()
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:  # Press any key to continue
                running = False """
import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')

font = os.path.join('resources', 'Roboto-Regular.ttf')

running = True

class EndScreen:
    def __init__(self, screen, message="You Lost!!", sub_message="Press any key to continue"):
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('resources', 'Roboto-Regular.ttf'), 50)
        self.sub_font = pygame.font.Font(os.path.join('resources', 'Roboto-Regular.ttf'), 30)
        self.message = message
        self.sub_message = sub_message

    def display(self):
        self.screen.fill((255, 255, 255))  # Screen color
        text = self.font.render(self.message, True, (0, 0, 0))  # Main message
        text_rect = text.get_rect(center=(1280 // 2, 720 // 2 - 30))
        self.screen.blit(text, text_rect)
        
        sub_text = self.sub_font.render(self.sub_message, True, (100, 100, 100))  # Sub message
        sub_text_rect = sub_text.get_rect(center=(1280 // 2, 900 // 2 + 30)) 
        self.screen.blit(sub_text, sub_text_rect)
        
        pygame.display.flip()  # Make sure the screen updates with the new content
end_screen = EndScreen(screen)
end_screen.display() 

while running:
    # Display the end screen continuously in order to fill conditions for any updates to the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:  # Press any key to continu
            #THIS IS TO INSERT START SCREENe
            screen.fill((0, 0, 0))  # Clear the screen after the key press (optional)
            pygame.display.flip()  # Update the display after clearing
""" class EndScreen:
    def __init__(self, screen, message="You Lost!!"):
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('resources', 'Roboto-Regular.ttf'), 50)
        self.message = message

    def display(self):
        self.screen.fill((255, 255, 255))  # Screen color
        text = self.font.render(self.message, True, (0, 0, 0))  # Text colors
        text_rect = text.get_rect(center=(1280 // 2, 720 // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        sub_text = self.sub_font.render(self.sub_message, True, (100, 100, 100))  # Sub message
        sub_text_rect = sub_text.get_rect(center=(1280 // 2, 720 // 2 + 30))
        self.screen.blit(sub_text, sub_text_rect)

game_over_screen = EndScreen(screen)
game_over_screen.display()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:  # Press any key to continue
            running = False """

""" class EndScreen:
    def __init__(self, screen, message="You Lost!!"):
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('resources', 'Roboto-Regular.ttf'), 50)
        self.message = message
        self.running = True

    def display(self):
        self.screen.fill((255, 255, 255)) #screen color
        text = self.font.render(self.message, True, (0, 0, 0))  #text colors
        text_rect = text.get_rect(center=(1280 // 2, 720 // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:  # Press any key to continue
                    running = False """