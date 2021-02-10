def is_palindrome(data):
    if not isinstance(data, str) and not isinstance(data, int):
        raise TypeError()

    if not data:
        raise ValueError()

    if isinstance(data, int):
        data = str(data)

    data = "".join([x.lower() for x in data if x.isalpha() or x.isdigit()])
    
    return data == data[::-1]

test_cases = {
    ''   : ValueError,
    10   : False,
    11   : True,
    'a': True,
    'aa': True,
    'aba': True,
    'abba': True,
    'abcba': True,
    'abca': False,
    'Sore was I ere I saw Eros.': True,
    '"Stop!" nine myriad murmur. "Put up rum, rum, dairymen, in pots."': True,
    '1a1': True,
    '2137': False
}

for data, expectation in test_cases.items():
    print ('----------')
    print (type(expectation))
    if expectation in (ValueError,TypeError):
        try:
            response = is_palindrome(data)
            print(f'Expected {expectation!r} for {data!r} got {response!r}')
        except expectation:
            pass
    else:
        response = is_palindrome(data)
        assert response == expectation, \
            f'Expected {expectation!r} for {data!r} got {response!r}'