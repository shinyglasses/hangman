import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Start_Screen:

    def make_hangman():
        body_parts = [
            {'type': 'circle', 'pos': (1000, 100), 'radius': 50},  # head
            {'type': 'line', 'start_pos': (1000, 149), 'end_pos': (1000, 300), 'width': 20},  # body
            {'type': 'line', 'start_pos': (1000, 210), 'end_pos': (950, 250), 'width': 20},  # left arm
            {'type': 'line', 'start_pos': (1000, 210), 'end_pos': (1050, 250), 'width': 20},  # right arm
            {'type': 'line', 'start_pos': (1000, 300), 'end_pos': (950, 400), 'width': 20},  # left leg
            {'type': 'line', 'start_pos': (1000, 300), 'end_pos': (1050, 400), 'width': 20},  # right leg
                ]
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
        elif event.type == pygame.KEYDOWN:  # Press any key to continu
            #THIS IS TO INSERT START SCREENe
            pass
             # Clear the screen after the key press (optional)
    pygame.display.flip()  # Update the display after clearing