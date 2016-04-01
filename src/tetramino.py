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
