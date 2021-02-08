import pytest
 
def prime_factors(number):
    if type(number) != int:
        raise TypeError("only integers > 1 can be factorized")

    if number <= 1:
        raise ValueError("only integers > 1 can be factorized")

    sito_eratostenesa = [True] * (number+1)
    output = []
    for i in range(2, number+1):
        if sito_eratostenesa[i]:
            if number%i == 0:
                output.append(i)
                for j in range(i,number+1,i):
                    sito_eratostenesa[j] = False

    return output
def test_type():
    with pytest.raises(TypeError):
        prime_factors(None)

def test_range():
    with pytest.raises(ValueError):
        prime_factors(-10)

def test_one():
    with pytest.raises(ValueError):
        prime_factors(1)

def test_two():
    assert prime_factors(2) == [2]

def test_three():
    assert prime_factors(3) == [3]

def test_four():
    assert prime_factors(4) == [2]
