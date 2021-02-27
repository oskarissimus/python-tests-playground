from typing import Literal, Union

class Converter:
    def __init__(self):
        self.roman_to_decimal_mapping = {
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
        self.decimal_to_roman_mapping = {value:key for key, value in self.roman_to_decimal_mapping.items()}
        self.decimal_values_of_legal_roman_symbols = list(self.decimal_to_roman_mapping)


    def convert_decimal_to_roman(self, number: int):
        if number < 1:
            raise ValueError('cant convert non-positive number to roman')
        roman_number = ''
        while number > 0:
            biggest_decimal_value_of_legal_roman_symbol_lower_than_number =\
                max([n for n in self.decimal_values_of_legal_roman_symbols if n<=number])
            roman_number += self.decimal_to_roman_mapping[biggest_decimal_value_of_legal_roman_symbol_lower_than_number]
            number -= biggest_decimal_value_of_legal_roman_symbol_lower_than_number
        return roman_number


    def convert_roman_to_decimal(self, number: str):    
        # validating number
        legal_roman_symbols = 'IVXLCDM'
        for c in number:
            if c not in legal_roman_symbols:
                raise ValueError(f'number in roman numeral system must consists of "{legal_roman_symbols}"')

        decimal_number = 0
        i = 0
        while i < len(number):

            #checking if order of symbol is descending
            if i+1 < len(number):
                if self.roman_to_decimal_mapping[number[i]] >= self.roman_to_decimal_mapping[number[i+1]]:
                    #order is ok
                    decimal_number += self.roman_to_decimal_mapping[number[i]]
                    i += 1
                else:
                    #order is bad, but it could be one of double-char symbols
                    double_char_roman_symbol = number[i:i+2]
                    if double_char_roman_symbol in self.roman_to_decimal_mapping.keys():
                        decimal_number += self.roman_to_decimal_mapping[double_char_roman_symbol]
                        i += 2
                    else:
                        raise ValueError('order of roman symbols in number must be descending')
            else:
                decimal_number += self.roman_to_decimal_mapping[number[i]]
                i+=1
        if number == self.convert_decimal_to_roman(decimal_number):
            return decimal_number
        else:
            raise ValueError('wrong format of number')


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


    c = Converter()

    if source_numeral_system == 'decimal':
        return c.convert_decimal_to_roman(number)

    elif source_numeral_system == 'roman':
        return c.convert_roman_to_decimal(number)


