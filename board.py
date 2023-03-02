import pygame
import numpy as np
from utils import draw_chessboard, draw_pieces, show_possible_moves
from piece import Piece,Pawn, Rook, Knight, Bishop, Queen, King
pygame.init()
clock = pygame.time.Clock()
run = True
selected = False
not_selected_row = 0
not_selected_column = 0
selected_row = 0
selected_column = 0
turn = 'w'

window = pygame.display.set_mode((820,820))
pygame.display.set_caption('Chess')

chessboard = np.array([
    [Rook(0, 0, 'b'),Knight(0, 1, 'b'),Bishop(0, 2,'b'),Queen(0,3, 'b'),King(0, 4, 'b'),Bishop(0, 5, 'b'),Knight(0, 6, 'b'),Rook(0, 7, 'b')],
    [Pawn(1, 0, 'b'),Pawn(1, 1, 'b'),Pawn(1, 2, 'b'),Pawn(1, 3, 'b'),Pawn(1, 4, 'b'),Pawn(1, 5, 'b'),Pawn(1, 6, 'b'),Pawn(1, 7, 'b')],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [Pawn(6, 0, 'w'),Pawn(6, 1, 'w'),Pawn(6, 2, 'w'),Pawn(6, 3, 'w'),Pawn(6, 4, 'w'),Pawn(6, 5, 'w'),Pawn(6, 6, 'w'),Pawn(6, 7, 'w')],
    [Rook(7, 0, 'w'),Knight(7, 1, 'w'),Bishop(7, 2,'w'),Queen(7,3, 'w'),King(7, 4, 'w'),Bishop(7, 5, 'w'),Knight(7, 6, 'w'),Rook(7, 7, 'w')]
])

window.fill((200,200,200))
draw_chessboard(window)
draw_pieces(window, chessboard)

while run:
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            if not selected:
                x_pos, y_pos = pygame.mouse.get_pos()
                not_selected_row = int((y_pos - 90) / 80)
                not_selected_column = int((x_pos - 90) / 80)
                if isinstance(chessboard[not_selected_row, not_selected_column], Piece):
                    if chessboard[not_selected_row, not_selected_column].color == turn:
                        possible_moves = chessboard[not_selected_row, not_selected_column].indicate_possible_moves(
                            chessboard)
                        selected = True
                        show_possible_moves(window, possible_moves)

            elif selected:
                x_pos, y_pos = pygame.mouse.get_pos()
                selected_row = int((y_pos - 90) / 80)
                selected_column = int((x_pos - 90) / 80)
                if (selected_row, selected_column) in possible_moves:
                    if isinstance(chessboard[selected_row, selected_column],Rook) and isinstance(chessboard[not_selected_row, not_selected_column], King):
                        rook = chessboard[selected_row,selected_column]
                        king = chessboard[not_selected_row, not_selected_column]
                        if rook.moved == False and king.moved == False and rook.color == king.color and king.castled == False:
                            king.moved = True
                            rook.moved = True
                            king.castled = True
                            if selected_column > not_selected_column:
                                king.column = not_selected_column + 2
                                rook.column = not_selected_column + 1

                                chessboard[not_selected_row,not_selected_column + 2] = king
                                chessboard[not_selected_row, not_selected_column + 1] = rook
                                chessboard[not_selected_row, not_selected_column ] = 0
                                chessboard[selected_row, selected_column] = 0
                            else:
                                king.column = not_selected_column - 2
                                rook.column = not_selected_column - 1

                                chessboard[not_selected_row,not_selected_column - 2] = king
                                chessboard[not_selected_row, not_selected_column - 1] = rook
                                chessboard[not_selected_row, not_selected_column] = 0
                                chessboard[selected_row, selected_column] = 0

                    else:
                        chessboard[not_selected_row,
                                    not_selected_column].row = selected_row
                        chessboard[not_selected_row,
                                    not_selected_column].column = selected_column
                        chessboard[selected_row,
                                    selected_column] = chessboard[not_selected_row, not_selected_column]
                        chessboard[not_selected_row, not_selected_column] = 0
                        if isinstance(chessboard[selected_row, selected_column], Pawn):
                            chessboard[selected_row, selected_column].moved = True
                        elif isinstance(chessboard[selected_row, selected_column], Rook):
                            chessboard[selected_row, selected_column].moved = True
                        elif isinstance(chessboard[selected_row, selected_column], King):
                            chessboard[selected_row, selected_column].moved = True

                    if turn == 'w':
                        turn = 'b'
                    else:
                        turn = 'w'

                selected = False
                draw_chessboard(window)
                draw_pieces(window, chessboard)

        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
    