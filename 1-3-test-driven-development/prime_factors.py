import pytest
import math

def prime_factors(number):
    if type(number) != int:
        raise TypeError("only integers > 1 can be factorized")

    if number <= 1:
        raise ValueError("only integers > 1 can be factorized")

    sito_eratostenesa = [True] * (number+1)
    output = []
    #i thought it was mem error, but before i got to mem problem, performance stopped me on 1bil
    #i think it would be ok to check numbers only to sqrt(number)
    for i in range(2, int(math.sqrt(number))+2):
        if sito_eratostenesa[i]:
            if number%i == 0:
                output.append(i)
                for j in range(i,len(sito_eratostenesa),i):
                    sito_eratostenesa[j] = False

    #number is prime
    if output == []:
        return [number]
    else:
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

def test_five():
    assert prime_factors(5) == [5]

def test_six():
    assert prime_factors(6) == [2,3]

def test_yellow():
    assert prime_factors(2137) == [2137]

def test_if_i_got_enough_mem_for_10k():
    assert prime_factors(10000) == [2,5]

def test_if_i_got_enough_mem_for_1m():
    assert prime_factors(10**6) == [2,5]

def test_if_i_got_enough_mem_for_10m():
    assert prime_factors(10**7) == [2,5]

def test_if_i_got_enough_mem_for_100m():
    assert prime_factors(10**8) == [2,5]

def test_some_crazy_number():
    assert prime_factors(3958159172) == [2, 11, 2347, 38329]
