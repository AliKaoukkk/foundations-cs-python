def digitCount(n):
    if n < 10:
        return 1
    else:
        return 1 + digitCount(n / 10)


user_input = int(input('enter a message'))
result = digitCount(user_input)
print('number of digits in ', user_input, 'is', result)