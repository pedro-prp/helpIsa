x = input('First number: ')
y = input('Second number: ')

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
    res = -1

if(res != -1):
    print(f'Result = {res}')