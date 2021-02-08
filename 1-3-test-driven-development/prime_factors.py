import pytest
 
def prime_factors(number):
    if type(number) != int:
        raise TypeError()   
    return

def test_type():
    with pytest.raises(TypeError):
        prime_factors(None)