import numpy as np


class Game:
    def __init__(self):
        self.board = np.array([
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ])
        self.whiteTurn = True  # white has to move
        '''Keep track of king's location'''
        self.whiteKing = (7, 4)
        self.blackKing = (0, 4)
        self.check = False
        self.check_mate = False
        self.stale_mate = False
        self.moveLog = []  # list of moves that were made

    def makeMove(self, move):
        # checks if the right piece was selected (white while white's turn or black while black's turn)
        if (self.whiteTurn and move.moved_piece[0] == 'w') or (not self.whiteTurn and move.moved_piece[0] == 'b'):
            if move.moved_piece[1] == 'P':  # if the moved piece is a pawn and has reached the back rank
                if (move.moved_piece[0] == 'w' and move.end_row == 0) or \
                        (move.moved_piece[0] == 'b' and move.end_row == 7):
                    move.moved_piece = move.moved_piece[0] + 'Q'  # pawn becomes a queen
                    move.promote = True
            self.board[move.end_row][move.end_col] = move.moved_piece
            self.board[move.start_row][move.start_col] = "**"
            if move.moved_piece == 'wK':
                self.whiteKing = (move.end_row, move.end_col)
            elif move.moved_piece == 'bK':
                self.blackKing = (move.end_row, move.end_col)
            # Check if the move has delivered a check
            self.whiteTurn = not self.whiteTurn
            self.moveLog.append(move)
        # else does nothing

    def moveBack(self):  # undoes the last move
        if len(self.moveLog) != 0:  # checks to see if a move has been made
            move = self.moveLog.pop()
            if move.promote:
                move.moved_piece = move.moved_piece[0] + 'P'
            self.board[move.start_row][move.start_col] = move.moved_piece
            self.board[move.end_row][move.end_col] = move.captured_piece  # if no piece captured restores blank
            if move.moved_piece == 'wK':
                self.whiteKing = (move.start_row, move.start_col)
            elif move.moved_piece == 'bK':
                self.blackKing = (move.start_row, move.start_col)
            self.whiteTurn = not self.whiteTurn  # changes player's turn
            self.check_mate = False
            self.stale_mate = False

    def moveForward(self):  # maybe add later
        pass

    '''
    This method checks if a move is valid. It calls another method
    that generates all possible moves considering the rules for each piece
    '''
    def getValidMoves(self):
        all_moves = self.generateMoves()
        for i in range(len(all_moves)-1, -1, -1):  # go through the list backwards
            # make this current move
            self.makeMove(all_moves[i])
            # change turn to check if in check
            self.whiteTurn = not self.whiteTurn
            # if in check then remove this move and then undo the move
            if self.kingUnderAttack():
                all_moves.remove(all_moves[i])
            self.whiteTurn = not self.whiteTurn
            self.moveBack()
        if len(all_moves) == 0:
            if self.kingUnderAttack():
                self.check_mate = True
            else:
                self.stale_mate = True
        else:
            self.check_mate = False
            self.stale_mate = False
        return all_moves


    def kingUnderAttack(self):
        # generate all opponent's moves
        row = 0
        col = 0
        if self.whiteTurn:
            row = self.whiteKing[0]
            col = self.whiteKing[1]
        elif not self.whiteTurn:
            row = self.blackKing[0]
            col = self.blackKing[1]
        self.whiteTurn = not self.whiteTurn
        opponent_moves = self.generateMoves()
        for move in opponent_moves:
            if move.end_row == row and move.end_col == col:
                self.whiteTurn = not self.whiteTurn
                return True
        self.whiteTurn = not self.whiteTurn
        return False



    def generateMoves(self):
        movelist = []  # list containing the possible moves
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                piece_color = self.board[i][j][0]  # 'w' or 'b'
                if (piece_color == 'w' and self.whiteTurn) or (piece_color == 'b' and not self.whiteTurn):
                    piece = self.board[i][j][1]  # P, R, N, B, K, Q
                    if piece == 'P':  # the piece is a pawn
                        self.generatePawnMoves(i, j, movelist)
                    elif piece == 'R':
                        self.generateRookMoves(i, j, movelist)
                    elif piece == 'N':
                        self.generateKnightMoves(i, j, movelist)
                    elif piece == 'B':
                        self.generateBishopMoves(i, j, movelist)
                    elif piece == 'Q':
                        self.generateQueenMoves(i, j, movelist)
                    elif piece == 'K':
                        self.generateKingMoves(i, j, movelist)
        return movelist
    '''
    These methods generate valid moved for a certain piece and stores them in the movelist variable
    The methods are to be called by self.generateMoves()
    '''

    def generatePawnMoves(self, row, col, movelist):
        piece_color = self.board[row][col][0]
        value = 0
        if piece_color == 'w':
            if row == 6 and self.board[row - 2][col] == '**':
                movelist.append(Move((row, col), (row-2, col), self.board))
            value = -1
        elif piece_color == 'b':
            if row == 1 and self.board[row + 2][col] == '**':
                movelist.append(Move((row, col), (row + 2, col), self.board))
            value = 1
        if self.board[row + value][col] == '**':  # square in front of pawn is empty
            movelist.append(Move((row, col), (row + value, col), self.board))
        '''Pawn capture moves'''
        if col != 0:
            if self.board[row + value][col - 1] != '**' and self.board[row + value][col - 1][0] != piece_color:  # pawn can capture a piece to it's left
                movelist.append(Move((row, col), (row + value, col - 1), self.board))
        if col != 7:
            if self.board[row + value][col + 1] != '**' and self.board[row + value][col + 1][0] != piece_color:  # pawn can capture a piece to it's right
                movelist.append(Move((row, col), (row + value, col + 1), self.board))
            # do en passant move later if there's time left

    def generateRookMoves(self, row, col, movelist):
        piece_color = self.board[row][col][0]
        if row + 1 < len(self.board):  # rook can move down the board
            for i in range(row + 1, len(self.board)):
                '''Check to see if piece is the same color'''
                if self.board[i][col][0] != piece_color:
                    movelist.append(Move((row, col), (i, col), self.board))
                if self.board[i][col] != '**':  # the rook can not jump over pieces
                    break
        if row - 1 >= 0:  # rook can move up the board
            for i in range(row - 1, -1, -1):
                if self.board[i][col][0] != piece_color:
                    movelist.append(Move((row, col), (i, col), self.board))
                if self.board[i][col] != '**':
                    break
        if col + 1 < 8:  # rook can move to the right
            for i in range(col + 1, len(self.board)):
                if self.board[row][i][0] != piece_color:
                    movelist.append(Move((row, col), (row, i), self.board))
                if self.board[row][i] != '**':
                    break
        if col - 1 >= 0:  # rook can move to the left
            for i in reversed(range(col)):
                if self.board[row][i][0] != piece_color:
                    movelist.append(Move((row, col), (row, i), self.board))
                if self.board[row][i] != '**':
                    break

    def generateKnightMoves(self, row, col, movelist):
        piece_color = self.board[row][col][0]
        for i in range(1, -2, -1):
            if i == 0:
                continue
            end_row = row + i*2
            end_col = col + i
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                if self.board[end_row][end_col][0] != piece_color:
                    movelist.append(Move((row, col), (end_row, end_col), self.board))
            end_row = row + i
            end_col = col + i*2
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                if self.board[end_row][end_col][0] != piece_color:
                    movelist.append(Move((row, col), (end_row, end_col), self.board))
        for i in range(1, -2, -1):
            if i == 0:
                continue
            end_row = row + i
            end_col = col - i*2
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                if self.board[end_row][end_col][0] != piece_color:
                    movelist.append(Move((row, col), (end_row, end_col), self.board))
            end_row = row + i*2
            end_col = col - i
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                if self.board[end_row][end_col][0] != piece_color:
                    movelist.append(Move((row, col), (end_row, end_col), self.board))

    def generateBishopMoves(self, row, col, movelist):
        piece_color = self.board[row][col][0]
        directions = ((-1, -1), (-1, 1), (1, 1), (1, -1))  # 4 diagonals
        for d in directions:
            for i in range(1, 8):
                end_row = row + d[0]*i
                end_col = col + d[1]*i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    if self.board[end_row][end_col] == '**':  # empty sq is ok
                        movelist.append(Move((row, col), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col][0] != piece_color:  # can't attack own color
                        movelist.append(Move((row, col), (end_row, end_col), self.board))
                        break  # piece captured can't go further on this direction
                    else:
                        break
                else:
                    break  # off the board


    def generateQueenMoves(self, row, col, movelist):
        piece_color = self.board[row][col][0]
        directions = ((-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (1, 0), (0, 1))  # all directions
        for d in directions:
            for i in range(1, 8):
                end_row = row + d[0]*i
                end_col = col + d[1]*i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    if self.board[end_row][end_col] == '**':  # empty sq is ok
                        movelist.append(Move((row, col), (end_row, end_col), self.board))
                    elif self.board[end_row][end_col][0] != piece_color:  # can't attack own color
                        movelist.append(Move((row, col), (end_row, end_col), self.board))
                        break  # piece captured can't go further on this direction
                    else:
                        break
                else:
                    break  # off the board

    def generateKingMoves(self, row, col, movelist):
        piece_color = self.board[row][col][0]
        directions = ((-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (1, 0), (0, 1))  # all directions
        for d in directions:
                end_row = row + d[0]
                end_col = col + d[1]
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    if self.board[end_row][end_col][0] != piece_color:  # empty sq is ok
                        movelist.append(Move((row, col), (end_row, end_col), self.board))
                else:
                    continue  # off the board


"""
This will be made by Antonia
This class should allow the ChessMain script to move pieces
and it should also change the game.board array
"""
class Move:
    def __init__(self, start, end, board):
        self.start_col = start[1]
        self.start_row = start[0]
        self.end_col = end[1]
        self.end_row = end[0]
        self.moved_piece = board[self.start_row][self.start_col]  # remember what piece has to be moved
        self.captured_piece = board[self.end_row][self.end_col]  # in case a piece has been captured#
        self.promote = False

    def __eq__(self, other):  # allows comparing two moves
        if isinstance(other, Move):  # makes sure that other is an instance of the class Move
            return (self.start_row == other.start_row and self.start_col == other.start_col and
                    self.end_row == other.end_row and self.end_col == other.end_col)
        return False