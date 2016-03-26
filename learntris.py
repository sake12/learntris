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
        else:
            print("Wrong code!")

if __name__ == '__main__':
    main()
