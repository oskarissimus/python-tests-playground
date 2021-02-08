def is_palindrome(data):
    if type(data) != str:
        raise TypeError()

    if data == '':
        raise ValueError()

    left = 0
    right = len(data)-1
    while left < right:
        if data[left] != data[right]:
            return False
        left  += 1
        right -= 1
    return True

test_cases = {
    ''   : ValueError,
    10   : TypeError,
    'a': True,
    'aa': True,
    'aba': True,
    'abba': True,
    'abcba': True,
    'abca': False,
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