a = int(input('Введите первое число: '))
b = int (input('Введите второе число: '))
c = int (input('Введите третье число: '))
if b != 0:
    if a % b == c:
        print('Утверждение верно')
    else:
        print('Утверждение неверно')
else:
    print('Делить на ноль нельзя!')