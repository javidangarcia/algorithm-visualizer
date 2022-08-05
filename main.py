import pygame
from pathfinding.constants import *
from pathfinding.blocks import Block

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra Algorithm Visualizer")

canvas = []
queue = []
path = []

for col in range(COLS):
    blocks = []
    for row in range(ROWS):
        blocks.append(Block(col, row))
    canvas.append(blocks)

for col in range(COLS):
    for row in range(ROWS):
        canvas[col][row].set_neighbors(canvas)

start_block = canvas[0][0]
start_block.start = True
start_block.visited = True
queue.append(start_block)

def main():
    begin_search = False
    target_block_set = False
    searching = True
    target_block = None

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if event.buttons[0]:
                    col = x // BLOCK_WIDTH
                    row = y // BLOCK_HEIGHT
                    canvas[col][row].wall = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN and target_block_set == False:
                    if event.button == 3:
                        col = x // BLOCK_WIDTH
                        row = y // BLOCK_HEIGHT
                        target_block = canvas[col][row]
                        target_block.target = True
                        target_block_set = True
            
            elif event.type == pygame.KEYDOWN and target_block_set:
                begin_search = True

        if begin_search:
            if len(queue) > 0 and searching:
                current_block = queue.pop(0)
                current_block.visited = True
                if current_block == target_block:
                    searching = False
                    while current_block.prior != start_block:
                        path.append(current_block.prior)
                        current_block = current_block.prior
                else:
                    for neighbor in current_block.neighbors:
                        if neighbor.queued == False and neighbor.wall == False:
                            neighbor.queued = True
                            neighbor.prior = current_block
                            queue.append(neighbor)
            else:
                if searching:
                    run = False

        WINDOW.fill(BLACK)
        for col in range(COLS):
            for row in range(ROWS):
                block = canvas[col][row]
                block.draw(WINDOW, GRAY)
                if block.queued:
                    block.draw(WINDOW, RED)
                if block.visited:
                    block.draw(WINDOW, GREEN)
                if block in path:
                    block.draw(WINDOW, BLUE)
                if block.start:
                    block.draw(WINDOW, BLUE)
                if block.wall:
                    block.draw(WINDOW, WHITE)
                if block.target:
                    block.draw(WINDOW, BLUE)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()