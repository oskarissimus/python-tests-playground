import pytest
from numsysconv.core import convert_numeral_system

def test_convertion_of_one_from_decimal_to_roman():
    assert convert_numeral_system(source_numeral_system='decimal',
                                  target_numeral_system='roman',
                                  number=1) == 'I'

def test_convertion_of_one_from_roman_to_decimal():
    assert convert_numeral_system(source_numeral_system='roman',
                                  target_numeral_system='decimal',
                                  number='I') == 1

class TestNumeralSystemNamingValidation:

    def test_source_numeral_system_naming_validation_accept_decimal(self):
        assert convert_numeral_system(source_numeral_system='decimal',
                                      target_numeral_system='roman',
                                      number=1) == 'I'

    def test_source_numeral_system_naming_validation_accept_roman(self):
        assert convert_numeral_system(source_numeral_system='roman',
                                      target_numeral_system='decimal',
                                      number='I') == 1

    def test_source_numeral_system_naming_validation_reject_bad_name(self):
        with pytest.raises(ValueError):
            convert_numeral_system(source_numeral_system='deci=====mal',
                                   target_numeral_system='roman',
                                   number=1)


    def test_target_numeral_system_naming_validation_accept_decimal(self):
        assert convert_numeral_system(source_numeral_system='decimal',
                                      target_numeral_system='roman',
                                      number=1) == 'I'

    def test_target_numeral_system_naming_validation_accept_roman(self):
        assert convert_numeral_system(source_numeral_system='roman',
                                      target_numeral_system='decimal',
                                      number='I') == 1

    def test_target_numeral_system_naming_validation_reject_bad_name(self):
        with pytest.raises(ValueError):
            convert_numeral_system(source_numeral_system='roman',
                                   target_numeral_system='deci=====mal',
                                   number='I')

