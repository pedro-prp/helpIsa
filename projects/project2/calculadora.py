
while True:
    x = int(input('First number: '))
    y = int(input('Second number: '))

    op = input('Select operation(+, -, *, \\): ')

    if(op == '+'):
        res = x + y
    elif(op == '-'):
        res = x - y
    elif(op == '*'):
        res = x * y
    elif(op == '/'):
        res = x / y
    else:
        print('Invalid Operation')
    
    print(chr(27) + "[2J")
    print(f'Result = {res}')
    decision = input('Make another operation?(Y/n): ')

    if decision == 'n':
        break