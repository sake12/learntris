class Tetramino:
    """ The tetramino """
    shapes = [[]]
    state = 0
    row = 0
    column = 0

    def rotate(self):
        self.state = (self.state + 1) % len(self.shapes)

    def get_current(self):
        return self.shapes[self.state]

    def get_position(self):
        return self.row, self.column


class TetraminoI(Tetramino):
    """ The I tetramino """
    row = 0
    column = 3
    shapes = [
        [[".", ".", ".", "."],
         ["c", "c", "c", "c"],
         [".", ".", ".", "."],
         [".", ".", ".", "."]],

        [[".", ".", "c", "."],
         [".", ".", "c", "."],
         [".", ".", "c", "."],
         [".", ".", "c", "."]],

        [[".", ".", ".", "."],
         [".", ".", ".", "."],
         ["c", "c", "c", "c"],
         [".", ".", ".", "."]],

        [[".", "c", ".", "."],
         [".", "c", ".", "."],
         [".", "c", ".", "."],
         [".", "c", ".", "."]]
    ]


class TetraminoO(Tetramino):
    """ The O tetramino """
    row = 0
    column = 4
    shapes = [
        [["y", "y"],
         ["y", "y"]]
    ]


class TetraminoZ(Tetramino):
    """ The Z tetramino """
    row = 0
    column = 3
    shapes = [
        [["r", "r", "."],
         [".", "r", "r"],
         [".", ".", "."]],

        [[".", ".", "r"],
         [".", "r", "r"],
         [".", "r", "."]],

        [[".", ".", "."],
         ["r", "r", "."],
         [".", "r", "r"]],

        [[".", "r", "."],
         ["r", "r", "."],
         ["r", ".", "."]]
    ]


class TetraminoS(Tetramino):
    """ The S tetramino """
    row = 0
    column = 3
    shapes = [
        [[".", "g", "g"],
         ["g", "g", "."],
         [".", ".", "."]],

        [[".", "g", "."],
         [".", "g", "g"],
         [".", ".", "g"]],

        [[".", ".", "."],
         [".", "g", "g"],
         ["g", "g", "."]],

        [["g", ".", "."],
         ["g", "g", "."],
         [".", "g", "."]]
    ]


class TetraminoJ(Tetramino):
    """ The J tetramino """
    row = 0
    column = 3
    shapes = [
        [["b", ".", "."],
         ["b", "b", "b"],
         [".", ".", "."]],

        [[".", "b", "b"],
         [".", "b", "."],
         [".", "b", "."]],

        [[".", ".", "."],
         ["b", "b", "b"],
         [".", ".", "b"]],

        [[".", "b", "."],
         [".", "b", "."],
         ["b", "b", "."]]
    ]


class TetraminoL(Tetramino):
    """ The L tetramino """
    row = 0
    column = 3
    shapes = [
        [[".", ".", "o"],
         ["o", "o", "o"],
         [".", ".", "."]],

        [[".", "o", "."],
         [".", "o", "."],
         [".", "o", "o"]],

        [[".", ".", "."],
         ["o", "o", "o"],
         ["o", ".", "."]],

        [["o", "o", "."],
         [".", "o", "."],
         [".", "o", "."]]
    ]


class TetraminoT(Tetramino):
    """ The T tetramino """
    row = 0
    column = 3
    shapes = [
        [[".", "m", "."],
         ["m", "m", "m"],
         [".", ".", "."]],

        [[".", "m", "."],
         [".", "m", "m"],
         [".", "m", "."]],

        [[".", ".", "."],
         ["m", "m", "m"],
         [".", "m", "."]],

        [[".", "m", "."],
         ["m", "m", "."],
         [".", "m", "."]]
    ]
