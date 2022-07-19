import pygame
from constants import *
from box import Box

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

grid = []
for col in range(COLS):
    boxes = []
    for row in range(ROWS):
        boxes.append(Box(col, row))
    grid.append(boxes)

start_box = grid[0][0]
start_box.start = True

def main():
    begin_search = False
    target_box_set = False

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()

                if event.buttons[0]:
                    col = x // BOX_WIDTH
                    row = y // BOX_HEIGHT
                    grid[col][row].wall = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN and target_box_set == False:
                    if event.button == 3:
                        col = x // BOX_WIDTH
                        row = y // BOX_HEIGHT
                        target_box = grid[col][row]
                        target_box.target = True
                        target_box_set = True
            
            elif event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True


        WINDOW.fill(BLACK)

        for col in range(COLS):
            for row in range(ROWS):
                box = grid[col][row]
                box.draw(WINDOW, GRAY)
                if box.start:
                    box.draw(WINDOW, BLUE)
                if box.wall:
                    box.draw(WINDOW, WHITE)
                if box.target:
                    box.draw(WINDOW, RED)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()