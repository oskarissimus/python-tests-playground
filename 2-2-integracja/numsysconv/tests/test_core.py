import pytest
from numsysconv.core import convert_numeral_system

def test_convertion_of_one_from_decimal_to_roman():
    assert convert_numeral_system(source_numeral_system='decimal',
                           destination_numeral_system='roman',
                           number=1) == 'I'