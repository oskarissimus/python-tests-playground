

def tic_tac_toe_winner(board):
    return 'X'

test_cases = {
    'XO  X O X': 'X',
    'OX  O X O': 'O',
    'XXOOXXXOO': None
}

for board, expectation in test_cases.items():
    assert tic_tac_toe_winner(board) == expectation, \
        f'Expected {expectation!r} for {board!r} got {response!r}'