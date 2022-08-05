from pathfinding.constants import *
import pygame

class Block:
    def __init__(self, col, row):
        self.x = col
        self.y = row
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbors = []
        self.prior = None

    def set_neighbors(self, canvas):
        if self.x > 0:
            self.neighbors.append(canvas[self.x - 1][self.y])
        if self.x < COLS - 1:
            self.neighbors.append(canvas[self.x + 1][self.y])
        if self.y > 0:
            self.neighbors.append(canvas[self.x][self.y - 1])
        if self.y < ROWS - 1:
            self.neighbors.append(canvas[self.x][self.y + 1])

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x * BLOCK_WIDTH, self.y * BLOCK_HEIGHT, BLOCK_WIDTH - 2, BLOCK_HEIGHT - 2))