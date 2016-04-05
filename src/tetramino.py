class Tetramino:
    def show_tetramino(self):
        pass


class TetraminoI(Tetramino):
    """ The I tetramino """
    def __init__(self):
        self.tetramino = [["."] * 4, ["c"] * 4, ["."] * 4, ["."] * 4]

    def show_tetramino(self):
        for a in self.tetramino:
            for b in a:
                print(b + " ", end="")
            print("")


class TetraminoO(Tetramino):
    """ The O tetramino """
    def __init__(self):
        self.tetramino = [["y"] * 2, ["y"] * 2]

    def show_tetramino(self):
        for a in self.tetramino:
            for b in a:
                print(b + " ", end="")
            print("")


class TetraminoZ(Tetramino):
    """ The Z tetramino """
    def __init__(self):
        self.tetramino = [["r", "r", "."], [".", "r", "r"], ["."] * 3]

    def show_tetramino(self):
        for a in self.tetramino:
            for b in a:
                print(b + " ", end="")
            print("")


class TetraminoS(Tetramino):
    """ The S tetramino """
    def __init__(self):
        self.tetramino = [[".", "g", "g"], ["g", "g", "."], ["."] * 3]

    def show_tetramino(self):
        for a in self.tetramino:
            for b in a:
                print(b + " ", end="")
            print("")


class TetraminoJ(Tetramino):
    """ The J tetramino """
    def __init__(self):
        self.tetramino = [["b", ".", "."], ["b"] * 3, ["."] * 3]

    def show_tetramino(self):
        for a in self.tetramino:
            for b in a:
                print(b + " ", end="")
            print("")


class TetraminoL(Tetramino):
    """ The L tetramino """
    def __init__(self):
        self.tetramino = [[".", ".", "o"], ["o"] * 3, ["."] * 3]

    def show_tetramino(self):
        for a in self.tetramino:
            for b in a:
                print(b + " ", end="")
            print("")


class TetraminoT(Tetramino):
    """ The T tetramino """
    def __init__(self):
        self.tetramino = [[".", "m", "."], ["m"] * 3, ["."] * 3]

    def show_tetramino(self):
        for a in self.tetramino:
            for b in a:
                print(b + " ", end="")
            print("")
