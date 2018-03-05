def adder(n):
    if n == 0:
        return 0

    # n = n - 1

    return n + adder(n - 1)


if __name__ == '__main__':
    print('''
    Give a number between 1 and 1000. We will count the sum
    1 + 2 + ... + N
    ''')
    number = int(input('> Input a number: '))
    total = adder(number)
    print total
