from copy import deepcopy


class GameException(Exception):
    pass


class Game(object):

    @staticmethod
    def result(state: list[list[str]], action: tuple[int, int], player: str) -> list[list[str]]:
        new_state: list[list[str]] = deepcopy(state)
        new_state[action[0]][action[1]] = player
        return new_state
    
    @staticmethod
    def actions(state: list[list[str]]) -> list[tuple[int, int]]:
        actions: list[tuple[int, int]] = []
        for i, row in enumerate(state):
            for j, col in enumerate(row):
                if col == ' ':
                    actions.append((i, j))
        return actions
    
    @staticmethod
    def terminal(state: list[list[str]]) -> bool:
        if all(state[i][j] != ' ' for i in range(3) for j in range(3)):
            return True

        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] and state[i][0] != ' ':
                return True
            if state[0][i] == state[1][i] == state[2][i] and state[0][i] != ' ':
                return True

        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != ' ':
            return True
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != ' ':
            return True
                
        return False
    
    @staticmethod
    def utility(state: list[list[str]], max_: str, min_: str, start: str) -> tuple[int, tuple[int, int]]:
        if all(state[i][j] != ' ' for i in range(3) for j in range(3)):
            return 0, (-1, -1)
        
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] and state[i][0] != ' ':
                if state[i][0] == max_: return 1, (-1, -1)
                else: return -1, (-1, -1)
            if state[0][i] == state[1][i] == state[2][i] and state[0][i] != ' ':
                if state[0][i] == max_: return 1, (-1, -1)
                else: return -1, (-1, -1)

        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != ' ':
            if state[0][0] == max_: return 1, (-1, -1)
            else: return -1, (-1, -1)
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != ' ':
            if state[0][2] == max_: return 1, (-1, -1)
            else: return -1, (-1, -1)

        turn: str = Game.player(state, max_, min_, start)
        actions: list[tuple[int, int]] = Game.actions(state)

        if turn == max_:
            maximum_action: tuple[int, int] = (-1, -1)
            maximum_value: int = -1000
            for action in actions:
                value, _ = Game.utility(Game.result(state, action, turn), max_, min_, start)
                if value > maximum_value:
                    maximum_value = value
                    maximum_action = action
            return maximum_value, maximum_action
                
        else:
            minimum_action: tuple[int, int] = (-1, -1)
            minimum_value: int = 1000
            for action in actions:
                value, _ = Game.utility(Game.result(state, action, turn), max_, min_, start)
                if value < minimum_value:
                    minimum_value = value
                    minimum_action = action
            return minimum_value, minimum_action
    
    @staticmethod
    def player(state: list[list[str]], max_: str, min_: str, start: str) -> str:
        max_count: int = 0
        min_count: int = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == max_: max_count += 1
                if state[i][j] == min_: min_count += 1
        if min_count == max_count:
            return start
        else:
            return max_ if min_ == start else min_

    @staticmethod
    def print(state: list[list[str]]) -> None:
        print()
        for i, row in enumerate(state):
            print('|'.join(row))
            if i != 2: print('-+-+-')
        print()
