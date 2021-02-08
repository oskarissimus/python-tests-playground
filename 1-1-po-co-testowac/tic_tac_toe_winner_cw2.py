import numpy as np

def tic_tac_toe_winner(board):
    #print (board)
    #validating input
    if len(board) != 9:
        raise ValueError()

    for character in board:
        if character not in ('X','O',' '):
            raise ValueError()

    board = np.array(list(board))
    npboard = board.reshape(3,3)
    win_list_X = ['X','X','X']
    win_list_O = ['O','O','O']

    #checking rows
    for row in 0,1,2:
        if list(npboard[row]) == win_list_X:
            return 'X'
        elif list(npboard[row]) == win_list_O:
            return 'O'

    #checking cols
    for col in 0,1,2:
        if list(npboard[:,col]) == win_list_X:
            return 'X'
        elif list(npboard[:,col]) == win_list_O:
            return 'O'

    #checking diagonal lines
    diagonal_line_1 = [npboard[0,0],npboard[1,1],npboard[2,2]]
    diagonal_line_2 = [npboard[0,2],npboard[1,1],npboard[2,0]]
    if diagonal_line_1 == win_list_X or diagonal_line_2 == win_list_X:
        return 'X'

    if diagonal_line_1 == win_list_O or diagonal_line_2 == win_list_O:
        return 'O'

test_cases = {
    '         ': None,
    '2317     ': ValueError,
    'XXX      ': 'X',
    '   XXX   ': 'X',
    '      XXX': 'X',
    'OOO      ': 'O',
    '   OOO   ': 'O',
    '      OOO': 'O',
    'O  O  O  ': 'O',
    ' O  O  O ': 'O',
    '  O  O  O': 'O',
    'X  X  X  ': 'X',
    ' X  X  X ': 'X',
    '  X  X  X': 'X',
    'XO  X O X': 'X',
    'OX  O X O': 'O',
    'XXOOXXXOO': None,
}

for board, expectation in test_cases.items():
    response = tic_tac_toe_winner(board)
    assert response == expectation, \
        f'Expected {expectation!r} for {board!r} got {response!r}'