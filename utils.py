import pygame
from piece import Piece
pygame.init()

WHITE = (255,240,240)
BLACK = (180, 150, 120)

def draw_chessboard(window):
    i = 1
    x_pos, y_pos = 90,90
    for row in range(8):
        for column in range(8):
            if i == 1:
                pygame.draw.rect(window, WHITE, pygame.rect.Rect(x_pos, y_pos, 80, 80))
                i = -i
            else:
                pygame.draw.rect(window, BLACK, pygame.rect.Rect(x_pos, y_pos, 80, 80))
                i = -i

            x_pos += 80
        x_pos = 90
        y_pos += 80
        i = -i 

def draw_pieces(window,chessboard):
    for row in chessboard:
        for piece in row:
            if isinstance(piece, Piece):
                print(piece.id, end=" ")
                piece.draw(window)
            else:
                print(piece, end=" ")
        print()

def show_possible_moves(window,possible_moves):
    for coordinate in possible_moves:
        pygame.draw.circle(window, (200,0,0), (130 + 80 * coordinate[1], 130 + 80 * coordinate[0]), 5)