def convert_numeral_system(source_numeral_system,
                           target_numeral_system,
                           number):
    #validating imput
    if source_numeral_system not in ['decimal','roman']:
        raise ValueError('source_numeral_system has to be "decimal" or "roman"')

    if target_numeral_system not in ['decimal','roman']:
        raise ValueError('target_numeral_system has to be "decimal" or "roman"')

    if source_numeral_system == target_numeral_system:
        raise ValueError('target_numeral_system and source_numeral_system must differ')

    #some placeholders
    if number == 1:
        return 'I'
    
    if number == 'I':
        return 1
    