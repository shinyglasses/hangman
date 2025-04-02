import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Hangman:
  def __init__(self, word):
    self.word = word
    self.number_of_letters_right = 0
    self.limb_count = 0
    self.body_parts = [
    {'type': 'circle', 'pos': (1000, 100), 'radius': 50},  # head
    {'type': 'line', 'start_pos': (1000, 149), 'end_pos': (1000, 300), 'width': 20},  # body
    {'type': 'line', 'start_pos': (1000, 210), 'end_pos': (950, 250), 'width': 20},  # left arm
    {'type': 'line', 'start_pos': (1000, 210), 'end_pos': (1050, 250), 'width': 20},  # right arm
    {'type': 'line', 'start_pos': (1000, 300), 'end_pos': (950, 400), 'width': 20},  # left leg
    {'type': 'line', 'start_pos': (1000, 300), 'end_pos': (1050, 400), 'width': 20},  # right leg
        ]

  def display(self):
    pygame.draw.line(screen, 'black', (900, 50), (1000, 50), 20) #top bar of hanging thing
    pygame.draw.line(screen, 'black', (900, 41), (900, 450), 20) #long vertical bar of hanging thing
    pygame.draw.line(screen, 'black', (870, 450), (930, 450), 20) #bottom bar of hanging thing
    for limb in range(self.limb_count):
        part = self.body_parts[limb]
        if part['type'] == 'circle':
            pygame.draw.circle(screen, 'black', part['pos'], part['radius'])
        elif part['type'] == 'line':
            pygame.draw.line(screen, 'black', part['start_pos'], part['end_pos'], part['width'])
        elif limb == 6: #the user used all their attempts
           pass #insert end screen