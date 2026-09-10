import pygame
import random

pygame.init()

GRID_SIZE = 8
TILE_SIZE = 60
WIDTH = GRID_SIZE * TILE_SIZE
HEIGHT = GRID_SIZE * TILE_SIZE

BACKGROUND = (30, 30, 40)
GRID_LINE = (60, 60, 80)
SELECT_COLOR = (255, 255, 255)
CANDY_COLORS = [
    (231, 76, 60),
    (241, 196, 15),
    (46, 204, 113),
    (52, 152, 219),
    (155, 89, 182),
    (230, 126, 34),
]

board = [[random.randint(0, len(CANDY_COLORS) - 1) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

selected = None

def is_adjacent(pos1, pos2):
    row1, col1 = pos1
    row2, col2 = pos2
    return (abs(row1 - row2) == 1 and col1 == col2) or (abs(col1 - col2) == 1 and row1 == row2)

def swap_tiles(pos1, pos2):
    row1, col1 = pos1
    row2, col2 = pos2
    board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Match-3 Puzzle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            clicked_col = mouse_x // TILE_SIZE
            clicked_row = mouse_y // TILE_SIZE
            clicked_pos = (clicked_row, clicked_col)

            if selected is None:
                selected = clicked_pos
            else:
                if is_adjacent(selected, clicked_pos):
                    swap_tiles(selected, clicked_pos)
                selected = None

    screen.fill(BACKGROUND)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color_index = board[row][col]
            color = CANDY_COLORS[color_index]
            center_x = col * TILE_SIZE + TILE_SIZE // 2
            center_y = row * TILE_SIZE + TILE_SIZE // 2
            radius = TILE_SIZE // 2 - 6
            pygame.draw.circle(screen, color, (center_x, center_y), radius)

            if selected == (row, col):
                pygame.draw.circle(screen, SELECT_COLOR, (center_x, center_y), radius, 4)

    for row in range(GRID_SIZE + 1):
        pygame.draw.line(screen, GRID_LINE, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    for col in range(GRID_SIZE + 1):
        pygame.draw.line(screen, GRID_LINE, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

    pygame.display.flip()

pygame.quit()
