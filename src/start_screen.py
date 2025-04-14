
import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hangman")


class StartScreen:
    def __init__(self, screen):
        self.screen = screen

        # Fonts
        self.title_font = pygame.font.Font(None, 175)
        self.subtitle_font = pygame.font.Font(None, 150)
        self.button_font = pygame.font.Font(None, 100)
        self.tilted_font = pygame.font.Font(None, 40)
        self.bottom_font = pygame.font.Font(None, 30)

        # Button
        self.button_rect = pygame.Rect(490, 450, 300, 100)

    def draw_hangman(self):
        pygame.draw.line(self.screen, 'black', (100, 150), (200, 150), 20)
        pygame.draw.line(self.screen, 'black', (100, 141), (100, 550), 20)
        pygame.draw.line(self.screen, 'black', (70, 550), (130, 550), 20)
        pygame.draw.circle(self.screen, 'black', (200, 200), 50)
        pygame.draw.line(self.screen, 'black', (200, 249), (200, 400), 20)
        pygame.draw.line(self.screen, 'black', (200, 310), (150, 350), 20)
        pygame.draw.line(self.screen, 'black', (200, 310), (250, 350), 20)
        pygame.draw.line(self.screen, 'black', (200, 400), (150, 500), 20)
        pygame.draw.line(self.screen, 'black', (200, 400), (250, 500), 20)

    def draw_title(self):
        title_text = self.title_font.render("HANGMAN", True, 'black')
        title_rect = title_text.get_rect(center=(640, 175))
        self.screen.blit(title_text, title_rect)

        game_text = self.subtitle_font.render("GAME", True, 'black')
        game_rect = game_text.get_rect(center=(640, 325))
        self.screen.blit(game_text, game_rect)

    def draw_start_button(self):
        pygame.draw.rect(self.screen, 'black', self.button_rect, border_radius=25)
        pygame.draw.rect(self.screen, 'white', self.button_rect.inflate(-12, -12), border_radius=20)
        start_text = self.button_font.render("START", True, 'black')
        start_rect = start_text.get_rect(center=self.button_rect.center)
        self.screen.blit(start_text, start_rect)

    def draw_tilted_message(self):
        first_line = self.tilted_font.render("            Will you guess", True, 'black')
        second_line = self.tilted_font.render("the word?", True, 'black')
        rotated_first = pygame.transform.rotate(first_line, -20)
        rotated_second = pygame.transform.rotate(second_line, -20)
        first_rect = rotated_first.get_rect(center=(1050, 420))
        second_rect = rotated_second.get_rect(center=(1070, 460))
        self.screen.blit(rotated_first, first_rect)
        self.screen.blit(rotated_second, second_rect)

    def draw_bottom_text(self):
        bottom_text = self.bottom_font.render("Created by Nelson Ouyang and Crystal Lin", True, 'black')
        bottom_rect = bottom_text.get_rect(center=(650, 690))
        self.screen.blit(bottom_text, bottom_rect)
running = True
# Create an instance of the screen

while running:
    start_screen = StartScreen(screen)
    screen.fill('white')  # Set background to white
    start_screen.draw_hangman()
    start_screen.draw_title()
    start_screen.draw_start_button()
    start_screen.draw_tilted_message()
    start_screen.draw_bottom_text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen.button_rect.collidepoint(event.pos):
                screen.fill('black') 
                pygame.display.flip()
                running = False

    pygame.display.flip()