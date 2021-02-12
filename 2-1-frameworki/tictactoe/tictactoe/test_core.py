from tictactoe.core import tic_tac_toe_winner
test_cases = {
    '         ': None,
    '': ValueError,
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

    print ('-------------')
    print (f'|{board}|')
    if expectation == ValueError:
        try:
            response = tic_tac_toe_winner(board)
            print(f'Expected {expectation!r} for {board!r} got {response!r}')
        except expectation:
            pass
    else:
        response = tic_tac_toe_winner(board)
        assert response == expectation, \
            f'Expected {expectation!r} for {board!r} got {response!r}'