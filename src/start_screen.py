""" import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Start_Screen:

    def make_hangman():
        
        pygame.draw.line(screen, 'black', (100, 150), (200, 150), 20) #top bar of hanging thing
        pygame.draw.line(screen, 'black', (100, 141), (100, 550), 20) #long vertical bar of hanging thing
        pygame.draw.line(screen, 'black', (70, 550), (130, 550), 20) #bottom bar of hanging thing

        pygame.draw.circle(screen, 'black', (200, 200), 50) #head
        pygame.draw.line(screen, 'black', (200,249), (200,400), 20) #body
        pygame.draw.line(screen, 'black', (200, 310), (150, 350), 20) #left arm
        pygame.draw.line(screen, 'black', (200, 310), (250, 350), 20) #right arm 
        pygame.draw.line(screen, 'black', (200, 400), (150, 500), 20) #left leg
        pygame.draw.line(screen, 'black', (200, 400), (250,500), 20) #right leg

running = True
while running:
    screen.fill('white')
    Start_Screen.make_hangman()
    # Display the end screen continuously in order to fill conditions for any updates to the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()  # Update the display after clearing """

""" import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hangman")

# Set up fonts
pygame.font.init()
title_font = pygame.font.Font(None, 175)  # Large font for title
subtitle_font = pygame.font.Font(None, 150)  # Font for "Game"

class Start_Screen:
    def make_hangman():
        pygame.draw.line(screen, 'black', (100, 150), (200, 150), 20)  # Top bar of hanging thing
        pygame.draw.line(screen, 'black', (100, 141), (100, 550), 20)  # Long vertical bar of hanging thing
        pygame.draw.line(screen, 'black', (70, 550), (130, 550), 20)  # Bottom bar of hanging thing

        pygame.draw.circle(screen, 'black', (200, 200), 50)  # Head
        pygame.draw.line(screen, 'black', (200, 249), (200, 400), 20)  # Body
        pygame.draw.line(screen, 'black', (200, 310), (150, 350), 20)  # Left arm
        pygame.draw.line(screen, 'black', (200, 310), (250, 350), 20)  # Right arm
        pygame.draw.line(screen, 'black', (200, 400), (150, 500), 20)  # Left leg
        pygame.draw.line(screen, 'black', (200, 400), (250, 500), 20)  # Right leg
    def draw_text():
        # Render "HANGMAN" at the top
        hangman_text = title_font.render("HANGMAN", True, 'black')
        hangman_rect = hangman_text.get_rect(center=(640, 175))  # Centered at the top
        screen.blit(hangman_text, hangman_rect)

        # Render "GAME" at the bottom with space for a start button
        game_text = subtitle_font.render("GAME", True, 'black')
        game_rect = game_text.get_rect(center=(640, 325))  # Above where the button would be
        screen.blit(game_text, game_rect)

# Game loop
running = True
while running:
    screen.fill('white')  # Set background to white
    Start_Screen.make_hangman()  # Draw the hangman
    Start_Screen.draw_text()  # Draw the title and subtitle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()  # Update the display """

import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hangman")

# Set up fonts
pygame.font.init()
title_font = pygame.font.Font(None, 175)  # Large font for title
subtitle_font = pygame.font.Font(None, 150)  # Font for "Game"
button_font = pygame.font.Font(None, 100)  # Font for button text

# Button dimensions
button_rect = pygame.Rect(490, 450, 300, 100)  # (x, y, width, height)

class Start_Screen:
    def make_hangman():
        pygame.draw.line(screen, 'black', (100, 150), (200, 150), 20)  # Top bar of hanging thing
        pygame.draw.line(screen, 'black', (100, 141), (100, 550), 20)  # Long vertical bar of hanging thing
        pygame.draw.line(screen, 'black', (70, 550), (130, 550), 20)  # Bottom bar of hanging thing

        pygame.draw.circle(screen, 'black', (200, 200), 50)  # Head
        pygame.draw.line(screen, 'black', (200, 249), (200, 400), 20)  # Body
        pygame.draw.line(screen, 'black', (200, 310), (150, 350), 20)  # Left arm
        pygame.draw.line(screen, 'black', (200, 310), (250, 350), 20)  # Right arm
        pygame.draw.line(screen, 'black', (200, 400), (150, 500), 20)  # Left leg
        pygame.draw.line(screen, 'black', (200, 400), (250, 500), 20)  # Right leg

    def draw_text():
        # Render "HANGMAN" at the top
        hangman_text = title_font.render("HANGMAN", True, 'black')
        hangman_rect = hangman_text.get_rect(center=(640, 175))  # Centered at the top
        screen.blit(hangman_text, hangman_rect)

        # Render "GAME" in the middle
        game_text = subtitle_font.render("GAME", True, 'black')
        game_rect = game_text.get_rect(center=(640, 325))  # Above where the button would be
        screen.blit(game_text, game_rect)

    def draw_button():
        pygame.draw.rect(screen, 'black', button_rect, border_radius=25)  # Button outline
        pygame.draw.rect(screen, 'white', button_rect.inflate(-10, -10), border_radius=20)  # Inner part
        
        # Render "START" text in the button
        start_text = button_font.render("START", True, 'black')
        start_rect = start_text.get_rect(center=button_rect.center)
        screen.blit(start_text, start_rect)

# Game loop
running = True
while running:
    screen.fill('white')  # Set background to white
    Start_Screen.make_hangman()  # Draw the hangman
    Start_Screen.draw_text()  # Draw the title and subtitle
    Start_Screen.draw_button()  # Draw the start button

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):  # Check if click is inside the button
                screen.fill('black')  # Fill screen with black
                pygame.display.flip()  # Update the screen 
                running = False  # Exit loop

    pygame.display.flip()  # Update the display