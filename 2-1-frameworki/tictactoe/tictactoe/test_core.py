from tictactoe.core import tic_tac_toe_winner
import pytest

def test_empty_board():
    assert tic_tac_toe_winner(' '*9) == None

def test_empty_string_as_board():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('')

def test_yellow():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('2317     ')



def test_top_line_wins_X():
    assert tic_tac_toe_winner('XXX      ') == 'X'

def test_middle_line_wins_X():
    assert tic_tac_toe_winner('   XXX   ') == 'X'

def test_bottom_line_wins_X():
    assert tic_tac_toe_winner('      XXX') == 'X'



def test_top_line_wins_O():
    assert tic_tac_toe_winner('OOO      ') == 'O'

def test_middle_line_wins_O():
    assert tic_tac_toe_winner('   OOO   ') == 'O'

def test_bottom_line_wins_O():
    assert tic_tac_toe_winner('      OOO') == 'O'



def test_left_col_wins_X():
    assert tic_tac_toe_winner('X  X  X  ') == 'X'

def test_middle_col_wins_X():
    assert tic_tac_toe_winner(' X  X  X ') == 'X'

def test_right_col_wins_X():
    assert tic_tac_toe_winner('  X  X  X') == 'X'



def test_left_col_wins_O():
    assert tic_tac_toe_winner('O  O  O  ') == 'O'

def test_middle_col_wins_O():
    assert tic_tac_toe_winner(' O  O  O ') == 'O'

def test_right_col_wins_O():
    assert tic_tac_toe_winner('  O  O  O') == 'O'



def test_diagonal_1():
    assert tic_tac_toe_winner('XO  X O X') == 'X'

def test_diagonal_2():
    assert tic_tac_toe_winner('OX  O X O') == 'O'


def test_nobody_wins():
    assert tic_tac_toe_winner('XXOOXXXOO') == None
