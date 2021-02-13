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
        if number < 1:
            raise ValueError('cant convert non-positive number to roman')
        roman_number = ''
        while number > 0:
            biggest_decimal_value_of_legal_roman_symbol_lower_than_number =\
              max([n for n in decimal_values_of_legal_roman_symbols if n<=number])
            roman_number += decimal_to_roman_mapping[biggest_decimal_value_of_legal_roman_symbol_lower_than_number]
            number -= biggest_decimal_value_of_legal_roman_symbol_lower_than_number
        return roman_number

    elif source_numeral_system == 'roman':

        # validating number
        legal_roman_symbols = 'IVXLCDM'
        for c in number:
            if c not in legal_roman_symbols:
                raise ValueError(f'number in roman numeral system must consists of "{legal_roman_symbols}"')

        decimal_number = 0
        i = 0
        while i < len(number):
            roman_symbol = number[i]
            #checking if order of symbol is descending
            if i+1 < len(number):
                if roman_to_decimal_mapping[number[i]] >= roman_to_decimal_mapping[number[i+1]]:
                    #order is ok
                    decimal_number += roman_to_decimal_mapping[number[i]]
                    i += 1
                else:
                    #order is bad, but it could be one of double-char symbols
                    double_char_roman_symbol = number[i:i+2]
                    if double_char_roman_symbol in roman_to_decimal_mapping.keys():
                        decimal_number += roman_to_decimal_mapping[double_char_roman_symbol]
                        i += 2
                    else:
                        raise ValueError('order of roman symbols in number must be descending')
            else:
                decimal_number += roman_to_decimal_mapping[number[i]]
                i+=1
        if number == convert_numeral_system('decimal','roman',decimal_number):
            return decimal_number
        else:
            raise ValueError('wrong format of number')


