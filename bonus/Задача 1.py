mid = 0
n = 0
s = []
a = input('Введите число: ')
while a:
    b = ''
    b += a
    s.append(int(b))
    print(s)
    a = input('Введите число: ')
for i in s:
    mid += i
    n += 1
mid = mid/n
print('Среднее арифметическое введенных чисел:', mid)
print('Максимальное из введенных чисел: ', max(s))
print('Минимальное из введенных чисел: ', min(s))
