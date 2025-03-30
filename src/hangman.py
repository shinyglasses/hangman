import pygame

class Hangman:
  def __init__(self, word, number_of_letters_right):
    self.word = word
    self.number_of_letters_right = number_of_letters_right
    # probably add appearance attribute (function) once i coded it
  def dead(self):
    pass
  # create passive aggressive speech bubble messages (triangle + oval) when hangman is almost dead
