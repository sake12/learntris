import src.tetramino as tetra


class Board:
    """ Board """
    def __init__(self):
        self._board = [['.' for _ in range(10)] for _ in range(22)]
        self._score = 0
        self._cleared_lines = 0
        self._active_tetramino = tetra.Tetramino()

    def print_board(self):
        """ Show board on the screen """
        for a in self._board:
            for b in a:
                print(b + " ", end="")
            print("")

    def set_board(self, stuff):
        """ Fill board with given data """
        row = 0
        column = 0
        for a in stuff:
            for b in a.split(" "):
                self._board[row][column] = b
                column += 1
            column = 0
            row += 1

    def clear(self):
        self._board = [['.' for _ in range(10)] for _ in range(22)]

    def get_score(self):
        """ Return current score """
        return self._score

    def get_cleared_lines(self):
        """ Return how many lines have been cleared """
        return self._cleared_lines

    def run_one_step(self):
        """ Return how many lines have been cleared """
        for row in range(len(self._board)):
            if "." not in self._board[row]:
                self._board[row] = ["."] * 10
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

    def print_tetramino(self):
        """ Print active tetramino """
        self._active_tetramino.show_tetramino()
