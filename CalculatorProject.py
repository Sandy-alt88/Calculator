def checkZeroDivision(b):
    while b == 0:
        print('\nZero Division not allowed')
        b = int(input('\nEnter b: '))

    return b

def calculate(a, b, op):
    match op:
        case '+': return a+b
        case '-': return a-b
        case '*': return a*b
        case '/': return a/b
        case '//': return a//b
        case '%': return a%b
        case '**': return a**b

while True:
    try:
        a = int(input("\nEnter a: "))
        b = int(input("\nEnter b: "))
    except ValueError:
        print('\nPlease enter valid numbers')
        continue

    op = input("\nEnter operator (To exit, enter Q/q): ")

    if op.lower() == 'q': 
        print(f'\nExiting the calculator\n')
        break

    b = checkZeroDivision(b)
    res = calculate(a, b, op)
    print(f'\nResult is: {res}')