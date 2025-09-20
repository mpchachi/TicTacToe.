"""
Tic Tac Toe Player
"""

import math

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
    numx = sum(row.count("X") for row in board)
    numo = sum(row.count("O") for row in board)
    if numx <= numo:
        return "X"
    else:
        return "O"
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acciones = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
             acciones.add((i, j))
    return acciones


def result(board, action):
    if action is None or len(action) != 2:
        raise Exception("acción no válida")
    i, j = action
    if not isinstance(i, int) or not isinstance(j, int):
        raise Exception("acción no válida")
    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception("acción fuera de rango")
    if board[i][j] is not EMPTY:
        raise Exception("celda ocupada")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] is not None and all(cell == row[0] for cell in row):
            return row[0]
    for j in range(len(board[0])):
        column = [board[i][j] for i in range(len(board))]
        if column[0] is not None and all(cell == column[0] for cell in column):
            return column[0]

    if board[0][0] is not None and all(board[i][i] == board[0][0] for i in range(len(board))):
        return board[0][0]

    if board[0][2] is not None and all(board[i][2-i] == board[0][2] for i in range(len(board))):
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in {"X", "O"}: return True
    elif not any(EMPTY in row for row in board): return True
    
    
    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ganador = winner(board)
    match ganador:
        case "X":
            return 1
        case "O":
            return -1
        case None:
            return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    turn = player(board)
    if turn == "X":
        mejorv= float("-inf")
        mejora = None
        for a in actions(board):
            valor = MinValue(result(board, a))
            if valor > mejorv:
                mejorv = valor
                mejora = a
                if mejorv == 1:
                    break
        return mejora
    else:
        mejorv = float("inf")
        mejora = None
        for a in actions(board):
            val = MaxValue(result(board, a))
            if val < mejorv:
                mejorv = val
                mejora = a
                if mejorv == -1:
                    break
        return mejora

    raise NotImplementedError
def MaxValue(board):
    if terminal(board): return utility(board)

    v = float("-inf")
    
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
        
    return v
    ...
def MinValue(board):
    if terminal(board): return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v
