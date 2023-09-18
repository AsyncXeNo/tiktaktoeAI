import sys

from game.game import Game


def main() -> None:
    state: list[list[str]] = [['X', 'O', ' '],
                              ['X', 'O', 'X'],
                              ['O', 'X', ' ']]
    
    print(Game.utility(state, 'X', 'O', 'X'))

if __name__ == '__main__':
    main()