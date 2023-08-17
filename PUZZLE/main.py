import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the game window
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the game window
pygame.display.set_caption("Scrabble Slide Puzzle")

# Load the Scrabble board image
board_image = pygame.image.load("Doraemon_character.png")

# Define the size of each tile
TILE_SIZE = (board_image.get_width() // 4, board_image.get_height() // 4)

# Define the number of rows and columns in the puzzle
ROWS = 4
COLS = 4

# Create the list of tiles
tiles = []
for row in range(ROWS):
    for col in range(COLS):
        x = col * TILE_SIZE[0]
        y = row * TILE_SIZE[1]
        tile = board_image.subsurface(pygame.Rect(x, y, TILE_SIZE[0], TILE_SIZE[1]))
        tiles.append(tile)

# Create the list of tile positions
tile_positions = [(col, row) for row in range(ROWS) for col in range(COLS)]

# Randomly shuffle the tile positions
random.shuffle(tile_positions)

# Define the position of the blank tile
blank_position = (3, 3)

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the font
font = pygame.font.SysFont(None, 36)

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // TILE_SIZE[0]
            row = y // TILE_SIZE[1]
            if (col, row) in [(blank_position[0]-1, blank_position[1]), (blank_position[0]+1, blank_position[1]), (blank_position[0], blank_position[1]-1), (blank_position[0], blank_position[1]+1)]:
                i = tile_positions.index((col, row))
                blank_i = tile_positions.index(blank_position)
                tile_positions[i], tile_positions[blank_i] = tile_positions[blank_i], tile_positions[i]
                blank_position = (col, row)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the tiles
    for i, pos in enumerate(tile_positions):
        col, row = pos
        if pos != blank_position:
            x = col * TILE_SIZE[0]
            y = row * TILE_SIZE[1]
            screen.blit(tiles[i], (x, y))

    # Draw the tile numbers
    for i, pos in enumerate(tile_positions):
        col, row = pos
        if pos != blank_position:
            x = col * TILE_SIZE[0] + TILE_SIZE[0] // 2
            y = row * TILE_SIZE[1] + TILE_SIZE[1] // 2
            text = font.render(str(i + 1), True, BLACK)
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
