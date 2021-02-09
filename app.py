def calculator_interface():
    print_menu()
    N = int(input())
        
    while N != 3:
        if N == 1:
            sum_1_to_N()
        elif N == 2:
            expression()
        else:
            break
    
def print_menu():
    print('Enter 1 to sum numbers 1 to N: ')
    print('Enter 2 to perfor the calculation of an expression: ')
    print('Enter 3 to exit the Special Calculator: ')
    


def sum_1_to_N():
    N = int(input())
    sum = 0
    sum = N * (N+1) / 2
    print(f'The sum from 1 to N is 1: {sum}')
    calculator_interface()


def expression():
    res = 0
    a, operator, b = input('Enter a regular expression: ').split()
    a, b = float(a), float (b)

    if operator == '+':
        res = a + b
        print(f'{a} + {b} = {res}')
    elif operator == '-':
        res = a - b
        print(f'{a} - {b} = {res}')
    elif operator == '*':
        res = a * b
        print(f'{a} * {b} = {res}')
    elif operator == '**':
        res = a ** b
        print(f'{a} ** {b} = {res}')
    else:
        result = divide(a, operator, b)
    
    calculator_interface()


def divide(a, operator, b):
    product = 0
    if b == 0:
        print('not a valid entry!')
    else:
        product = a / b
    print(f'{a} / {b} = {product}')
calculator_interface()


    
        







   
            




