import pygame

class Piece:

    def __init__(self, row, column, color):
        self.color = color
        self.row = row
        self.column = column
        self.image = 0

    def draw(self, window):
        window.blit(self.image, (100 + 80 * self.column, 100 + 80 * self.row))


class Pawn(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color)
        self.moved = False
        if self.color == 'w':
            self.id = 1
            self.image = pygame.image.load('img/1_w_pawn.png')
        elif self.color == 'b':
            self.id = - 1
            self.image = pygame.image.load('img/1_b_pawn.png')

    def indicate_possible_moves(self, chessboard):
        possible_moves = []
        try:
            if not self.moved:
                if self.color == 'w':
                    if chessboard[self.row - 1, self.column] == 0:
                        possible_moves.append((self.row - 1, self.column))
                        if chessboard[self.row - 2, self.column] == 0:
                            possible_moves.append((self.row - 2, self.column))

                    if -1 < self.column - 1 < 8:
                        if chessboard[self.row - 1, self.column - 1] != 0:
                            if chessboard[self.row - 1, self.column - 1].id < 0:
                                print('girdi1')
                                possible_moves.append((self.row - 1, self.column - 1))

                    if -1 < self.column + 1 < 8:
                        if chessboard[self.row - 1, self.column + 1] != 0:
                            if chessboard[self.row - 1, self.column + 1].id < 0:
                                print('girdi4')
                                possible_moves.append((self.row - 1, self.column + 1))

                elif self.color == 'b':
                    if chessboard[self.row + 1, self.column] == 0:
                        possible_moves.append((self.row + 1, self.column))
                        if chessboard[self.row + 2, self.column] == 0:
                            possible_moves.append((self.row + 2, self.column))

                    if -1 < self.column - 1 < 8:
                        if chessboard[self.row + 1, self.column - 1] != 0:
                            if chessboard[self.row + 1, self.column - 1].id > 0:
                                possible_moves.append((self.row + 1, self.column - 1))

                    if -1 < self.column + 1 < 8:
                        if chessboard[self.row + 1, self.column + 1] != 0:
                            if chessboard[self.row + 1, self.column + 1].id > 0:
                                possible_moves.append((self.row + 1, self.column + 1))

            if self.moved:
                if self.color == 'w':
                    if chessboard[self.row - 1, self.column] == 0:
                        possible_moves.append((self.row - 1, self.column))

                    if self.column - 1 != -1:
                        if chessboard[self.row - 1, self.column - 1] != 0:
                            if chessboard[self.row - 1, self.column - 1].id < 0:
                                possible_moves.append(
                                    (self.row - 1, self.column - 1))

                    if self.column + 1 != 8:
                        if chessboard[self.row - 1, self.column + 1] != 0:
                            if chessboard[self.row - 1, self.column + 1].id < 0:
                                possible_moves.append(
                                    (self.row - 1, self.column + 1))

                elif self.color == 'b':
                    if chessboard[self.row + 1, self.column] == 0:
                        possible_moves.append((self.row + 1, self.column))

                    if self.column - 1 != -1:
                        if chessboard[self.row + 1, self.column - 1] != 0:
                            if chessboard[self.row + 1, self.column - 1].id > 0:
                                possible_moves.append(
                                    (self.row + 1, self.column - 1))

                    if self.column + 1 != 8:
                        if chessboard[self.row + 1, self.column + 1] != 0:
                            if chessboard[self.row + 1, self.column + 1].id > 0:
                                possible_moves.append(
                                    (self.row + 1, self.column + 1))
        except:
            pass
        return possible_moves


class Rook(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color)
        self.moved = False

        if self.color == 'w':
            self.id = 2
            self.image = pygame.image.load('img/9_w_rook.png')
        elif self.color == 'b':
            self.id = -2
            self.image = pygame.image.load('img/9_b_rook.png')

    def indicate_possible_moves(self, chessboard):
        possible_moves = []

        row = self.row
        column = self.column

        if self.color == 'w':
            while -1 < row + 1 < 8:
                if chessboard[row + 1, column] != 0:
                    if chessboard[row + 1, column].id < 0:
                        possible_moves.append((row + 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column))
                row += 1

            row = self.row

            while -1 < row - 1 < 8:
                if chessboard[row - 1, column] != 0:
                    if chessboard[row - 1, column].id < 0:
                        possible_moves.append((row - 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column))
                row -= 1

            row = self.row

            while -1 < column - 1 < 8:
                if chessboard[row, column - 1] != 0:
                    if chessboard[row, column - 1].id < 0:
                        possible_moves.append((row, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column - 1))
                column -= 1

            column = self.column

            while -1 < column + 1 < 8:
                if chessboard[row, column + 1] != 0:
                    if chessboard[row, column + 1].id < 0:
                        possible_moves.append((row, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column + 1))
                column += 1


        if self.color == 'b':
            while -1 < row + 1 < 8:
                if chessboard[row + 1, column] != 0:
                    if chessboard[row + 1, column].id > 0:
                        possible_moves.append((row + 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column))
                row += 1

            row = self.row

            while -1 < row - 1 < 8:
                if chessboard[row - 1, column] != 0:
                    if chessboard[row - 1, column].id > 0:
                        possible_moves.append((row - 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column))
                row -= 1

            row = self.row

            while -1 < column - 1 < 8:
                if chessboard[row, column - 1] != 0:
                    if chessboard[row, column - 1].id > 0:
                        possible_moves.append((row, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column - 1))
                column -= 1

            column = self.column

            while -1 < column + 1 < 8:
                if chessboard[row, column + 1] != 0:
                    if chessboard[row, column + 1].id > 0:
                        possible_moves.append((row, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column + 1))
                column += 1

        return possible_moves

class Knight(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color)

        if self.color == 'w':
            self.id = 3
            self.image = pygame.image.load('img/8_w_knight.png')
        elif self.color == 'b':
            self.id = - 3
            self.image = pygame.image.load('img/8_b_knight.png')

    def indicate_possible_moves(self, chessboard):
        possible_moves = []

        if self.color == 'w':
            if -1 < self.row - 2 < 8 and -1 < self.column - 1 < 8:
                if chessboard[self.row - 2, self.column - 1] != 0:
                    if chessboard[self.row - 2, self.column - 1].id < 0:
                        possible_moves.append(
                            (self.row - 2, self.column - 1))
                else:
                    possible_moves.append((self.row - 2, self.column - 1))

            if -1 < self.row - 2 < 8 and -1 < self.column + 1 < 8:
                if chessboard[self.row - 2, self.column + 1] != 0:
                    if chessboard[self.row - 2, self.column + 1].id < 0:
                        possible_moves.append(
                            (self.row - 2, self.column + 1))
                else:
                    possible_moves.append((self.row - 2, self.column + 1))

            if -1 < self.row + 2 < 8 and -1 < self.column - 1 < 8:
                if chessboard[self.row + 2, self.column - 1] != 0:
                    if chessboard[self.row + 2, self.column - 1].id < 0:
                        possible_moves.append(
                            (self.row + 2, self.column - 1))
                else:
                    possible_moves.append((self.row + 2, self.column - 1))

            if -1 < self.row + 2 < 8 and -1 < self.column + 1 < 8:
                if chessboard[self.row + 2, self.column + 1] != 0:
                    if chessboard[self.row + 2, self.column + 1].id < 0:
                        possible_moves.append(
                            (self.row + 2, self.column + 1))
                else:
                    possible_moves.append((self.row + 2, self.column + 1))

            if -1 < self.row + 1 < 8 and -1 < self.column + 2 < 8:
                if chessboard[self.row + 1, self.column + 2] != 0:
                    if chessboard[self.row + 1, self.column + 2].id < 0:
                        possible_moves.append(
                            (self.row + 1, self.column + 2))
                else:
                    possible_moves.append((self.row + 1, self.column + 2))

            if -1 < self.row + 1 < 8 and -1 < self.column - 2 < 8:
                if chessboard[self.row + 1, self.column - 2] != 0:
                    if chessboard[self.row + 1, self.column - 2].id < 0:
                        possible_moves.append(
                            (self.row + 1, self.column - 2))
                else:
                    possible_moves.append((self.row + 1, self.column - 2))

            if -1 < self.row - 1 < 8 and -1 < self.column + 2 < 8:
                if chessboard[self.row - 1, self.column + 2] != 0:
                    if chessboard[self.row - 1, self.column + 2].id < 0:
                        possible_moves.append(
                            (self.row - 1, self.column + 2))
                else:
                    possible_moves.append((self.row - 1, self.column + 2))

            if -1 < self.row - 1 < 8 and -1 < self.column - 2 < 8:
                if chessboard[self.row - 1, self.column - 2] != 0:
                    if chessboard[self.row - 1, self.column - 2].id < 0:
                        possible_moves.append(
                            (self.row - 1, self.column - 2))
                else:
                    possible_moves.append((self.row - 1, self.column - 2))

        if self.color == 'b':
            if -1 < self.row - 2 < 8 and -1 < self.column - 1 < 8:
                if chessboard[self.row - 2, self.column - 1] != 0:
                    if chessboard[self.row - 2, self.column - 1].id > 0:
                        possible_moves.append(
                            (self.row - 2, self.column - 1))
                else:
                    possible_moves.append((self.row - 2, self.column - 1))

            if -1 < self.row - 2 < 8 and -1 < self.column + 1 < 8:
                if chessboard[self.row - 2, self.column + 1] != 0:
                    if chessboard[self.row - 2, self.column + 1].id > 0:
                        possible_moves.append(
                            (self.row - 2, self.column + 1))
                else:
                    possible_moves.append((self.row - 2, self.column + 1))

            if -1 < self.row + 2 < 8 and -1 < self.column - 1 < 8:
                if chessboard[self.row + 2, self.column - 1] != 0:
                    if chessboard[self.row + 2, self.column - 1].id > 0:
                        possible_moves.append(
                            (self.row + 2, self.column - 1))
                else:
                    possible_moves.append((self.row + 2, self.column - 1))

            if -1 < self.row + 2 < 8 and -1 < self.column + 1 < 8:
                if chessboard[self.row + 2, self.column + 1] != 0:
                    if chessboard[self.row + 2, self.column + 1].id > 0:
                        possible_moves.append(
                            (self.row + 2, self.column + 1))
                else:
                    possible_moves.append((self.row + 2, self.column + 1))

            if -1 < self.row + 1 < 8 and -1 < self.column + 2 < 8:
                if chessboard[self.row + 1, self.column + 2] != 0:
                    if chessboard[self.row + 1, self.column + 2].id > 0:
                        possible_moves.append(
                            (self.row + 1, self.column + 2))
                else:
                    possible_moves.append((self.row + 1, self.column + 2))

            if -1 < self.row + 1 < 8 and -1 < self.column - 2 < 8:
                if chessboard[self.row + 1, self.column - 2] != 0:
                    if chessboard[self.row + 1, self.column - 2].id > 0:
                        possible_moves.append(
                            (self.row + 1, self.column - 2))
                else:
                    possible_moves.append((self.row + 1, self.column - 2))

            if -1 < self.row - 1 < 8 and -1 < self.column + 2 < 8:
                if chessboard[self.row - 1, self.column + 2] != 0:
                    if chessboard[self.row - 1, self.column + 2].id > 0:
                        possible_moves.append(
                            (self.row - 1, self.column + 2))
                else:
                    possible_moves.append((self.row - 1, self.column + 2))

            if -1 < self.row - 1 < 8 and -1 < self.column - 2 < 8:
                if chessboard[self.row - 1, self.column - 2] != 0:
                    if chessboard[self.row - 1, self.column - 2].id > 0:
                        possible_moves.append(
                            (self.row - 1, self.column - 2))
                else:
                    possible_moves.append((self.row - 1, self.column - 2))

        return possible_moves


class Bishop(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color)

        if self.color == 'w':
            self.id = 4
            self.image = pygame.image.load('img/7_w_bishop.png')
        elif self.color == 'b':
            self.id = - 4
            self.image = pygame.image.load('img/7_b_bishop.png')

    def indicate_possible_moves(self, chessboard):
        possible_moves = []
        row = self.row
        column = self.column

        if self.color == 'w':
            while -1 < row - 1 < 8 and -1 < column - 1 < 8:  # row-- column--
                if chessboard[row - 1, column - 1] != 0:
                    if chessboard[row - 1, column - 1].id < 0:
                        possible_moves.append((row - 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column - 1))
                row -= 1
                column -= 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column + 1 < 8:  # row++ column++
                if chessboard[row + 1, column + 1] != 0:
                    if chessboard[row + 1, column + 1].id < 0:
                        possible_moves.append((row + 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column + 1))
                row += 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row - 1 < 8 and -1 < column + 1 < 8:  # row-- column++
                if chessboard[row - 1, column + 1] != 0:
                    if chessboard[row - 1, column + 1].id < 0:
                        possible_moves.append((row - 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column + 1))
                row -= 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column - 1 < 8:  # row++ column--
                if chessboard[row + 1, column - 1] != 0:
                    if chessboard[row + 1, column - 1].id < 0:
                        possible_moves.append((row + 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column - 1))
                row += 1
                column -= 1

        if self.color == 'b':
            while -1 < row - 1 < 8 and -1 < column - 1 < 8:  # row-- column--
                if chessboard[row - 1, column - 1] != 0:
                    if chessboard[row - 1, column - 1].id > 0:
                        possible_moves.append((row - 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column - 1))
                row -= 1
                column -= 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column + 1 < 8:  # row++ column++
                if chessboard[row + 1, column + 1] != 0:
                    if chessboard[row + 1, column + 1].id > 0:
                        possible_moves.append((row + 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column + 1))
                row += 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row - 1 < 8 and -1 < column + 1 < 8:  # row-- column++
                if chessboard[row - 1, column + 1] != 0:
                    if chessboard[row - 1, column + 1].id > 0:
                        possible_moves.append((row - 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column + 1))
                row -= 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column - 1 < 8:  # row++ column--
                if chessboard[row + 1, column - 1] != 0:
                    if chessboard[row + 1, column - 1].id > 0:
                        possible_moves.append((row + 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column - 1))
                row += 1
                column -= 1

        return possible_moves


class Queen(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color)

        if self.color == 'w':
            self.id = 5
            self.image = pygame.image.load('img/6_w_queen.png')
        elif self.color == 'b':
            self.id = - 5
            self.image = pygame.image.load('img/6_b_queen.png')

    def indicate_possible_moves(self, chessboard):
        possible_moves = []

        row = self.row
        column = self.column
        
        if self.color == 'w':
            while -1 < row + 1 < 8:
                if chessboard[row + 1, column] != 0:
                    if chessboard[row + 1, column].id < 0:
                        possible_moves.append((row + 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column))
                row += 1

            row = self.row

            while -1 < row - 1 < 8:
                if chessboard[row - 1, column] != 0:
                    if chessboard[row - 1, column].id < 0:
                        possible_moves.append((row - 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column))
                row -= 1

            row = self.row

            while -1 < column - 1 < 8:
                if chessboard[row, column - 1] != 0:
                    if chessboard[row, column - 1].id < 0:
                        possible_moves.append((row, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column - 1))
                column -= 1

            column = self.column

            while -1 < column + 1 < 8:
                if chessboard[row, column + 1] != 0:
                    if chessboard[row, column + 1].id < 0:
                        possible_moves.append((row, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column + 1))
                column += 1

            column = self.column

            while -1 < row - 1 < 8 and -1 < column - 1 < 8:  # row-- column--
                if chessboard[row - 1, column - 1] != 0:
                    if chessboard[row - 1, column - 1].id < 0:
                        possible_moves.append((row - 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column - 1))
                row -= 1
                column -= 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column + 1 < 8:  # row++ column++
                if chessboard[row + 1, column + 1] != 0:
                    if chessboard[row + 1, column + 1].id < 0:
                        possible_moves.append((row + 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column + 1))
                row += 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row - 1 < 8 and -1 < column + 1 < 8:  # row-- column++
                if chessboard[row - 1, column + 1] != 0:
                    if chessboard[row - 1, column + 1].id < 0:
                        possible_moves.append((row - 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column + 1))
                row -= 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column - 1 < 8:  # row++ column--
                if chessboard[row + 1, column - 1] != 0:
                    if chessboard[row + 1, column - 1].id < 0:
                        possible_moves.append((row + 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column - 1))
                row += 1
                column -= 1

        if self.color == 'b':
            while -1 < row + 1 < 8:
                if chessboard[row + 1, column] != 0:
                    if chessboard[row + 1, column].id > 0:
                        possible_moves.append((row + 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column))
                row += 1

            row = self.row

            while -1 < row - 1 < 8:
                if chessboard[row - 1, column] != 0:
                    if chessboard[row - 1, column].id > 0:
                        possible_moves.append((row - 1, column))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column))
                row -= 1

            row = self.row

            while -1 < column - 1 < 8:
                if chessboard[row, column - 1] != 0:
                    if chessboard[row, column - 1].id > 0:
                        possible_moves.append((row, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column - 1))
                column -= 1

            column = self.column

            while -1 < column + 1 < 8:
                if chessboard[row, column + 1] != 0:
                    if chessboard[row, column + 1].id > 0:
                        possible_moves.append((row, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row, column + 1))
                column += 1

            column = self.column

            while -1 < row - 1 < 8 and -1 < column - 1 < 8:  # row-- column--
                if chessboard[row - 1, column - 1] != 0:
                    if chessboard[row - 1, column - 1].id > 0:
                        possible_moves.append((row - 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column - 1))
                row -= 1
                column -= 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column + 1 < 8:  # row++ column++
                if chessboard[row + 1, column + 1] != 0:
                    if chessboard[row + 1, column + 1].id > 0:
                        possible_moves.append((row + 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column + 1))
                row += 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row - 1 < 8 and -1 < column + 1 < 8:  # row-- column++
                if chessboard[row - 1, column + 1] != 0:
                    if chessboard[row - 1, column + 1].id > 0:
                        possible_moves.append((row - 1, column + 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row - 1, column + 1))
                row -= 1
                column += 1

            row = self.row
            column = self.column

            while -1 < row + 1 < 8 and -1 < column - 1 < 8:  # row++ column--
                if chessboard[row + 1, column - 1] != 0:
                    if chessboard[row + 1, column - 1].id > 0:
                        possible_moves.append((row + 1, column - 1))
                        break
                    else:
                        break
                else:
                    possible_moves.append((row + 1, column - 1))
                row += 1
                column -= 1

        return possible_moves

class King(Piece):
    def __init__(self, row, column, color):
        super().__init__(row, column, color)
        self.moved = False
        self.castled = False
        if self.color == 'w':
            self.id = 6
            self.image = pygame.image.load('img/5_w_king.png')
        elif self.color == 'b':
            self.id = - 6
            self.image = pygame.image.load('img/5_b_king.png')

    def indicate_possible_moves(self, chessboard):
        possible_moves = []

        row = self.row
        column = self.column

        if self.color == 'w': 
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if -1 < row + i < 8 and -1 < column + j < 8:
                        if (row + i, column + j) != (self.row, self.column):
                            if chessboard[row + i, column + j] != 0:
                                if chessboard[row + i, column + j].id < 0:
                                    possible_moves.append((row + i, column + j))
                            else:
                                possible_moves.append((row + i, column + j))
                        else:
                            continue

            if not self.castled:
                if not self.moved:
                    if chessboard[self.row, self.column + 1] == 0 and chessboard[self.row, self.column + 2] == 0:
                        if isinstance(chessboard[self.row, self.column + 3], Rook):
                            if chessboard[self.row, self.column + 3].moved == False:
                                possible_moves.append((self.row, self.column + 3))

                    if chessboard[self.row, self.column - 1] == 0 and chessboard[self.row, self.column - 2] == 0 and chessboard[self.row, self.column - 3] == 0:
                        if isinstance(chessboard[self.row, self.column - 4], Rook):
                            if chessboard[self.row, self.column - 4].moved == False:
                                possible_moves.append((self.row, self.column - 4))
                    

        elif self.color == 'b': 
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if -1 < row + i < 8 and -1 < column + j < 8:
                        if (row + i, column + j) != (self.row, self.column):
                            if chessboard[row + i, column + j] != 0:
                                if chessboard[row + i, column + j].id > 0:
                                    possible_moves.append((row + i, column + j))
                            else:
                                possible_moves.append((row + i, column + j))
                        else:
                            continue

            if not self.castled:
                if not self.moved:
                    if chessboard[self.row, self.column + 1] == 0 and chessboard[self.row, self.column + 2] == 0:
                        if isinstance(chessboard[self.row, self.column + 3], Rook):
                            if chessboard[self.row, self.column + 3].moved == False:
                                possible_moves.append((self.row, self.column + 3))

                    if chessboard[self.row, self.column - 1] == 0 and chessboard[self.row, self.column - 2] == 0 and chessboard[self.row, self.column - 3] == 0:
                        if isinstance(chessboard[self.row, self.column - 4], Rook):
                            if chessboard[self.row, self.column - 4].moved == False:
                                possible_moves.append((self.row, self.column - 4))

        return possible_moves

    def castle_short(self,chessboard):
        pass

    def castle_long(self,chessboard):
        pass