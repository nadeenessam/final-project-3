import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("cat & rat")
spaces = 2
tiles =7
tile_x = int(WIDTH / (tiles + spaces))
tile_y = int(tile_x)
initial_x = int(tile_x)
initial_y = int(tile_x)
line = 1

WHAITE = (255, 255, 255)
BLACK = (0, 0, 0)
AQUA = (0, 255, 255)
GREEN = (0, 128,0)
YELLOW=(255,222,173)
board = []
water = []
bridge = []
water_references = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    (1, 0), (1, 6), (2, 0), (2, 6), (3, 0), (3, 6), (4, 0),
    (4, 6), (5, 0), (5, 6),
    (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)
]

frame_height = int(WIDTH - 2 * tile_x + 5)
frame_width = frame_height
frame = pygame.Surface((frame_height, frame_width))
frame.fill(WHAITE)
frame_rect = frame.get_rect()
frame_rect.x = tile_x - 2
frame_rect.y = tile_x - 2

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def board_rects():
    global initial_x, initial_y, tile_x, tile_y
    for x in range(7):
        for y in range(7):
            a_rectangle = pygame.Rect(initial_x, initial_y,tile_x, tile_y)
            if (x, y) in water_references:
                water.append(a_rectangle)
            if (x, y) == (3, 6):
                bridge.append(a_rectangle)
            else:
                board.append(a_rectangle)
            initial_x += tile_x + line
        initial_x = tile_x
        initial_y += tile_y + line

def draw_board():
    
    pygame.draw.rect(win, WHAITE, frame_rect, 2)

    for rect in board:
        pygame.draw.rect(win, WHAITE, rect)

    for rect in water:
        pygame.draw.rect(win, AQUA, rect)

    pygame.draw.rect(win, GREEN, bridge[0])

def create_mouse():
    pass

board_rects()

while True:
    win.fill(BLACK)
    events()
    draw_board()
    pygame.display.update()