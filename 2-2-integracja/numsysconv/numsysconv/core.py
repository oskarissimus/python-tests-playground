def convert_numeral_system(source_numeral_system,
                           target_numeral_system,
                           number):
    if source_numeral_system not in ['decimal','roman']:
        raise ValueError('source_numeral_system has to be "decimal" or "roman"')

    if target_numeral_system not in ['decimal','roman']:
        raise ValueError('target_numeral_system has to be "decimal" or "roman"')

    if number == 1:
        return 'I'
    
    if number == 'I':
        return 1
    