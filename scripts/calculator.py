def calculator():
    operation = input('Please enter the operation you wish to apply +, -, *, /, ^ :')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
        print(number_1, '', operation, '', number_2)
        print(number_1 + number_2)

    elif operation == '-':
        print(number_1, '', operation, '', number_2)
        print(number_1 - number_2)

    elif operation == '*':
        print(number_1, '', operation, '', number_2)
        print(number_1 * number_2)

    elif operation == '/':
        print(number_1, '', operation, '', number_2)
        print(number_1 / number_2)

    elif operation == "^":
        print(number_1, '', operation, '', number_2)
        print(number_1 ** number_2)

    else:
        print('Please enter an operator like the shown examples!')

calculator()