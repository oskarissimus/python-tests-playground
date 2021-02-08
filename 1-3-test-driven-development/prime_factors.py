import pytest
 
def prime_factors(number):
    if type(number) != int:
        raise TypeError("only integers > 1 can be factorized")

    if number <= 1:
        raise ValueError("only integers > 1 can be factorized")

def test_type():
    with pytest.raises(TypeError):
        prime_factors(None)

def test_range():
    with pytest.raises(ValueError):
        prime_factors(-10)

def test_one():
    with pytest.raises(ValueError):
        prime_factors(1)
