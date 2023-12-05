mode = input("operation(+,-,*,/): ")
value2 = float(input("value2: "))
value3 = float(input("value3: "))

if mode == '+':
    print(f'{value2 + value3}')
elif mode == '-':
    print(f'{value2 + value3}')
elif mode == '*':
    print(f'{value2 * value3}')
elif mode == '/':
    print(f'{value2 / value3}')
else:
    print('input error!')