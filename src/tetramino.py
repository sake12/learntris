class Tetramino:
    """ The tetramino """
    tetramino = []
    shapes = []
    state = 0

    def show_tetramino(self):
        tetramino = self.shapes[self.state]
        for a in tetramino:
            for b in a:
                print(b + " ", end="")
            print("")

    def rotate(self):
        self.state = (self.state + 1) % len(self.shapes)
        self.tetramino = self.shapes[self.state]


class TetraminoI(Tetramino):
    """ The I tetramino """
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
    shapes = [
        [["y", "y"],
         ["y", "y"]]
    ]


class TetraminoZ(Tetramino):
    """ The Z tetramino """
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
