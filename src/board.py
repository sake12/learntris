import src.tetramino as tetra


class Board:
    """ Board """

    def __init__(self):
        self._board = [['.' for _ in range(10)] for _ in range(22)]
        self._score = 0
        self._cleared_lines = 0
        self._active_tetramino = tetra.Tetramino()

    def __add_tetramino_to_board(self):
        board = self._board
        tetramino = self._active_tetramino.get_current()
        pos_row, pos_column = self._active_tetramino.get_position()

        for row, pos in enumerate(tetramino):
            for column, sign in enumerate(pos):
                board[row + pos_row][column + pos_column] = str.upper(sign)

        return board

    def print_board(self):
        """ Show board on the screen """
        board = self._board
        tetramino = self._active_tetramino.get_current()

        if tetramino:
            board = self.__add_tetramino_to_board()

        for row in board:
            for column in row:
                print(column + " ", end="")
            print("")

    def set_board(self, data):
        """ Fill board with given data """
        for row, line in enumerate(data):
            for column, sign in enumerate(line.split(" ")):
                self._board[row][column] = sign

    def clear(self):
        """ Clear board, score and lines """
        self._board = [['.' for _ in range(10)] for _ in range(22)]
        self._score = 0
        self._cleared_lines = 0

    def get_score(self):
        """ Return current score """
        return self._score

    def get_cleared_lines(self):
        """ Return how many lines have been cleared """
        return self._cleared_lines

    def run_one_step(self):
        """ Run one step of the game """
        for number, row in enumerate(self._board):
            if "." not in row:
                self._board[number] = ["."] * 10
                self._cleared_lines += 1
                self._score += 100

    def set_tetramino(self, tetramino):
        """ Set active tetramino """
        if tetramino == "I":
            self._active_tetramino = tetra.TetraminoI()
        elif tetramino == "O":
            self._active_tetramino = tetra.TetraminoO()
        elif tetramino == "Z":
            self._active_tetramino = tetra.TetraminoZ()
        elif tetramino == "S":
            self._active_tetramino = tetra.TetraminoS()
        elif tetramino == "J":
            self._active_tetramino = tetra.TetraminoJ()
        elif tetramino == "L":
            self._active_tetramino = tetra.TetraminoL()
        elif tetramino == "T":
            self._active_tetramino = tetra.TetraminoT()
        else:
            print("Wrong tetramino code!")

    def rotate_current(self):
        """ Rotate active tetramino clockwise """
        self._active_tetramino.rotate()

    def print_tetramino(self):
        """ Print active tetramino """
        for row in self._active_tetramino.get_current():
            for cell in row:
                print(cell + " ", end="")
            print("")
