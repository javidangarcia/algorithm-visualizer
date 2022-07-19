import pygame
from constants import *

class Box:
    def __init__(self, col, row):
        self.x = col
        self.y = row

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x * BOX_WIDTH, self.y * BOX_HEIGHT, BOX_WIDTH - 2, BOX_HEIGHT - 2))