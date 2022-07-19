import pygame
from constants import *
from box import Box

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def create_grid():
    grid = []
    for row in range(ROWS):
        boxes = []
        for col in range(COLS):
            boxes.append(Box(col, row))
        grid.append(boxes)
    return grid

def main():
    grid = create_grid()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WINDOW.fill(BLACK)

        for row in range(ROWS):
            for col in range(COLS):
                box = grid[col][row]
                box.draw(WINDOW, GRAY)

        pygame.display.update()

if __name__ == "__main__":
    main()