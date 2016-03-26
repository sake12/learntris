class Board:
    """ Board """
    def __init__(self):
        self._board = [['' for _ in range(10)] for _ in range(22)]

    def print_board(self):
        """ Show board on the screen """
        for a in self._board:
            for b in a:
                if b == "":
                    print(". ", end="")
                else:
                    print(b + " ", end="")
            print("")
