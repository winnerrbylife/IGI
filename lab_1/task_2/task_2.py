def MyFunc(a,b,operation):
    if (operation=='and'):
        return a + b
    elif (operation=='sub'):
        return a - b
    elif (operation=='mult'):
        return a * b
    elif (operation=='div'):
        return a / b

def input_number():
    while True:
        x = input()
        if x.isdigit():
            return int(x)
        else:
            print("Ошибка, попробуйте ещё раз")

print("Введите 1-ое число:")
x = input_number()

print("Введите 2-ое число")
y = input_number()

print("Введите операцию:")
operat = input()

if operat != 'and' and operat != 'sub' and operat != 'mult' and operat != 'div':
    print("Введена неправильная операция")
elif operat == 'div' and y == 0:
    print("Деление на 0")
else:
    print("Результат:", MyFunc(x,y,operat))