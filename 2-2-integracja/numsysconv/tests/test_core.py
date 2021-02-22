import pytest
from numsysconv.core import convert_numeral_system


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


@pytest.mark.parametrize("test_input,expected", [
    (1, 'I'),
    (4, 'IV'),
    (16, 'XVI'),
    (19, 'XIX'),
    (1234, 'MCCXXXIV'),
    (321, 'CCCXXI'),
    (451, 'CDLI'),
    (1666, 'MDCLXVI'),
    (3999, 'MMMCMXCIX'),
    (2000, 'MM'),
    (3800, 'MMMDCCC'),
    ])
def test_convertions_to_roman(test_input, expected):
    assert convert_numeral_system('decimal','roman',test_input) == expected


@pytest.mark.parametrize("expected,test_input", [
    (1, 'I'),
    (4, 'IV'),
    (16, 'XVI'),
    (19, 'XIX'),
    (1234, 'MCCXXXIV'),
    (321, 'CCCXXI'),
    (451, 'CDLI'),
    (1666, 'MDCLXVI'),
    (3999, 'MMMCMXCIX'),
    (2000, 'MM'),
    (3800, 'MMMDCCC'),
    ])
def test_convertions_to_decimal(expected, test_input):
    assert convert_numeral_system('roman','decimal',test_input) == expected


@pytest.mark.parametrize("test_input", [
    'XIIIIII',
    'IIIIIIIIIIIIIIII',
    'VVVI',
    'XXXXIIIIIIIII',
    'IL',
    'XXXXVIIII',
    'XXXXIX',
    'XLIIIIIIIII',
    'XLVIIII',
    ])
def test_if_invalid_roman_number_raise_value_error(test_input):
        with pytest.raises(ValueError):
            assert convert_numeral_system('roman','decimal',test_input)


def test_value_range_of_convertion_to_roman():
    with pytest.raises(ValueError):
        assert convert_numeral_system('decimal','roman',-10)

def test_rejection_of_attempt_to_convert_some_stupid_string():
    with pytest.raises(ValueError):
        assert convert_numeral_system('roman','decimal','somestupudstring')

def test_two_way_convertion_from_1_to_3999():
    for n in range(1,3999):
        roman_n = convert_numeral_system('decimal','roman',n)
        assert n == convert_numeral_system('roman', 'decimal',roman_n)