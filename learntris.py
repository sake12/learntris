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
        else:
            print("Wrong code!")

if __name__ == '__main__':
    main()
