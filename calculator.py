def calculator():
    x = float(input('First number: '))
    operation = input('Operation Symbol: ')
    y = float(input('Second number: '))

    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            return 'Divide by 0 error'
        return x / y
    else:
        return 'Invalid operation'

print(calculator())