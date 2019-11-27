def is_digit(string, a, b, c):

    if not isinstance(a, int):
        return 'wrong type a'

    if string.isdigit():
        return True
    try:
        float(string)
        return True
    except ValueError:
        return False


print(bool(is_digit(input('??? '), 1, True, '3')))
кккыыыы = is_digit(input('??? '), '1', 123312, '3')
print(кккыыыы)
print(bool(кккыыыы))
