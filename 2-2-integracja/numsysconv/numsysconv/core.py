def convert_numeral_system(source_numeral_system,
                           target_numeral_system,
                           number):
    #validating input
    if source_numeral_system not in ['decimal','roman']:
        raise ValueError('source_numeral_system has to be "decimal" or "roman"')

    if target_numeral_system not in ['decimal','roman']:
        raise ValueError('target_numeral_system has to be "decimal" or "roman"')

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
    