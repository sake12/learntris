from src.board import *


def main():
    """ Main function """
    board = Board()
    while True:
        code = input()

        if code == "q":
            exit()
        elif code == "p":
            board.print_board()
        elif code == "g":
            inp = []
            for a in range(22):
                inp.append(input())
            board.set_board(inp)
        elif code == "c":
            board = Board()
        elif code == "?s":
            print(board.get_score())
        elif code == "?n":
            print(board.get_cleared_lines())
        elif code == "s":
            board.run_one_step()
        elif str.isupper(code):
            board.set_tetramino(code)
        elif code == "t":
            board.print_tetramino()
        else:
            raise ValueError("Wrong code!")

if __name__ == '__main__':
    main()
