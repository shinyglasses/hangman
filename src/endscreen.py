import pygame
import os

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hangman')
font = os.path.join('resources', 'Roboto-Regular.ttf')

class EndScreen:
    def draw_end_screen():
        screen.fill((255, 255, 255))  # Set background to white
        
        # Load fonts
        font = pygame.font.Font(None, 120)
        sub_font = pygame.font.Font(None, 50)
        subsub_font = pygame.font.Font(None, 40)
        
        # Render main message
        text = font.render("You Lost!!", True, (50, 50, 50))
        text_rect = text.get_rect(center=(640, 250))  # Centered at upper middle
        screen.blit(text, text_rect)
        
        # Render sub message
        sub_text = sub_font.render("Press any key to continue", True, (100, 100, 100))
        sub_text_rect = sub_text.get_rect(center=(640, 500))  # Positioned below the main message
        screen.blit(sub_text, sub_text_rect)

        subsub_text = subsub_font.render("(RIP STICKMAN)", True, (0, 0, 0))
        subsub_text_rect = subsub_text.get_rect(center=(640, 330))
        screen.blit(subsub_text, subsub_text_rect)

        #Render grave        
        image_path = os.path.join('resources', 'grave.png')  # Path to the skull image
        grave_image = pygame.image.load(image_path)  # Load the image
        grave_image = pygame.transform.scale(grave_image, (100, 100))
        grave_rect = grave_image.get_rect(center=(640,  410))
        screen.blit(grave_image, grave_rect)

    def draw_skulls():
        image_path = os.path.join('resources', 'skull.png')  # Path to the skull image
        skull_image = pygame.image.load(image_path)  # Load the image
        skull_image = pygame.transform.scale(skull_image, (90, 100))
        # Paste the skull image (example: positioned at the bottom center of the screen)
        rotated_skull_image = pygame.transform.rotate(skull_image, 15)  # Rotate by 15 degrees
        skull_rect = rotated_skull_image.get_rect(center=(1200, 600)) 
        screen.blit(rotated_skull_image, skull_rect)
        rotated_skull_image = pygame.transform.rotate(skull_image, 45)  
        skull_rect = rotated_skull_image.get_rect(center=(200, 400)) 
        screen.blit(rotated_skull_image, skull_rect)
        rotated_skull_image = pygame.transform.rotate(skull_image, 125) 
        skull_rect = rotated_skull_image.get_rect(center=(630, 100)) 
        screen.blit(rotated_skull_image, skull_rect)
        rotated_skull_image = pygame.transform.rotate(skull_image, 270) 
        skull_rect = rotated_skull_image.get_rect(center=(1000, 200)) 
        screen.blit(rotated_skull_image, skull_rect)
        rotated_skull_image = pygame.transform.rotate(skull_image, 176) 
        skull_rect = rotated_skull_image.get_rect(center=(100, 100)) 
        screen.blit(rotated_skull_image, skull_rect)
        rotated_skull_image = pygame.transform.rotate(skull_image, 90) 
        skull_rect = rotated_skull_image.get_rect(center=(640, 680)) 
        screen.blit(rotated_skull_image, skull_rect)
        pygame.display.flip()  # Update screen
    def display():
        EndScreen.draw_end_screen()
        EndScreen.draw_skulls()
        pygame.display.flip()