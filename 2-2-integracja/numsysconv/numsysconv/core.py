from typing import Literal, Union
def convert_numeral_system(source_numeral_system: Literal['decimal','roman'],
                           target_numeral_system: Literal['decimal','roman'],
                           number: Union[str,int]) -> Union[str,int]:
    #validating input
    legal_numeral_systems = ('decimal','roman')
    if source_numeral_system not in legal_numeral_systems:
        raise ValueError(f'source_numeral_system has to be one of {legal_numeral_systems}')

    if target_numeral_system not in legal_numeral_systems:
        raise ValueError(f'target_numeral_system has to be one of {legal_numeral_systems}')

    if source_numeral_system == target_numeral_system:
        raise ValueError('target_numeral_system and source_numeral_system must differ')

    if source_numeral_system == 'decimal' and not isinstance(number,int):
        raise TypeError('converting from decimal - number must be int')

    if source_numeral_system == 'roman' and not isinstance(number,str):
        raise TypeError('converting from roman numeral system - number must be string')


    #some placeholders
    if number == 1:
        return 'I'
    
    if number == 'I':
        return 1

    legal_roman_symbols = 'IVXLCDM'

    roman_to_decimal_mapping = {
        'I':  1,
        'IV': 4,
        'V':  5,
        'IX': 9,
        'X':  10,
        'XL': 40,
        'L':  50,
        'XC': 90,
        'C':  100,
        'CD': 400,
        'D':  500,
        'CM': 900,
        'M':  1000,
    }
    #swapping mapping
    decimal_to_roman_mapping = {value:key for key, value in roman_to_decimal_mapping.items()}
    decimal_values_of_legal_roman_symbols = list(decimal_to_roman_mapping.keys())

    if source_numeral_system == 'decimal':
        roman_number = ''
        while number > 0:
            biggest_decimal_value_of_legal_roman_symbol_lower_than_number =\
              max([n for n in decimal_values_of_legal_roman_symbols if n<=number])
            roman_number += decimal_to_roman_mapping[biggest_decimal_value_of_legal_roman_symbol_lower_than_number]
            number -= biggest_decimal_value_of_legal_roman_symbol_lower_than_number
        return roman_number

