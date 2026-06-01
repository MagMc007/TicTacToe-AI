"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count == o_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    turn = player(board)
    i, j = action

    board_copy = copy.deepcopy(board)
    board_copy[i][j] = turn

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # \
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    # /
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for r in board:
        for c in r:
            if c == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)

    if won == X:
        return 1
    
    if won == O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)

        v = -math.inf

        for action in actions(board):
            v = max(v, min_value(result(board, action)))

        return v


    def min_value(board):
        if terminal(board):
            return utility(board)

        v = math.inf

        for action in actions(board):
            v = min(v, max_value(result(board, action)))

        return v
    
    if terminal(board):
        return None

    turn = player(board)

    if turn == X:
        best_score = -math.inf
        best_action = None

        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

                if best_score == 1:
                    return best_action

        return best_action
    else:
        best_score = math.inf
        best_action = None

        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

                if best_score == -1:
                    return best_action

        return best_action