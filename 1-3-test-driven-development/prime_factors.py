import pytest
 
def prime_factors(number):
    if type(number) != int:
        raise TypeError()



def test_type():
    with pytest.raises(TypeError):
        prime_factors(None)

def test_range():
    with pytest.raises(ValueError):
        prime_factors(-10)