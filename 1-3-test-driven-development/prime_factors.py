import pytest
 
def prime_factors(number):
    if type(number) != int:
        raise TypeError("only positive integers can be factorized")

    if number <= 0:
        raise ValueError("only positive integers can be factorized")

def test_type():
    with pytest.raises(TypeError):
        prime_factors(None)

def test_range():
    with pytest.raises(ValueError):
        prime_factors(-10)