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


def test_rejection_of_pointless_convertion_dec_to_dec():
    with pytest.raises(ValueError):
        convert_numeral_system(source_numeral_system='decimal',
                                target_numeral_system='decimal',
                                number=1)

def test_rejection_of_pointless_convertion_rom_to_rom():
    with pytest.raises(ValueError):
        convert_numeral_system(source_numeral_system='roman',
                                target_numeral_system='roman',
                                number='I')

def test_rejection_of_non_string_roman_number():
    with pytest.raises(TypeError):
        convert_numeral_system(source_numeral_system='roman',
                        target_numeral_system='decimal',
                        number=1)

def test_rejection_of_non_int_decimal_number():
    with pytest.raises(TypeError):
        convert_numeral_system(source_numeral_system='decimal',
                        target_numeral_system='roman',
                        number='I')

class TestConvertionsToRoman:
    def test_proper_convertion_of_16_to_roman(self):
        assert convert_numeral_system('decimal','roman',16) == 'XVI'

    def test_1_improper_convertion_of_16_to_roman(self):
        assert convert_numeral_system('decimal','roman',16) != 'XIIIIII'

    def test_2_improper_convertion_of_16_to_roman(self):
        assert convert_numeral_system('decimal','roman',16) != 'IIIIIIIIIIIIIIII'

    def test_3_improper_convertion_of_16_to_roman(self):
        assert convert_numeral_system('decimal','roman',16) != 'VVVI'

    def test_proper_convertion_of_4_to_roman(self):
        assert convert_numeral_system('decimal','roman',4) == 'IV'

    def test_improper_convertion_of_4_to_roman(self):
        assert convert_numeral_system('decimal','roman',4) != 'IIII'

    def test_proper_convertion_of_19_to_roman(self):
        assert convert_numeral_system('decimal','roman',19) == 'XIX'

    def test_1_improper_convertion_of_19_to_roman(self):
        assert convert_numeral_system('decimal','roman',19) != 'IXX'

    def test_2_improper_convertion_of_19_to_roman(self):
        assert convert_numeral_system('decimal','roman',19) != 'XVIV'

    def test_4_improper_convertion_of_19_to_roman(self):
        assert convert_numeral_system('decimal','roman',19) != 'XIIIIIIIII'

    def test_5_improper_convertion_of_19_to_roman(self):
        assert convert_numeral_system('decimal','roman',19) != 'XVIIII'

class TestConvertionsToDecimal:

    def test_proper_convertion_of_XVI_to_decimal(self):
        assert convert_numeral_system('roman','decimal','XVI') == 16
