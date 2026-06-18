def triangular_pattern(n: int):
    for i in range(1, n + 1):
        print((n - i) * ' ' + ((2*i - 1) * '*') + ((n - i) * ' '))


def string_reversal(s: str):
    result = ''
    for i in range(1, len(s) + 1):
        result += s[-1 * i]
    
    print(result)


def main():
    triangular_pattern(int(input('Lines in pattern: ')))

    string_reversal(input('String to reverse: '))

main()

