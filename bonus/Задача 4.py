alpf = "аеёиоуыэюя"
w = input('Введите слово кириллицей: ')
for i in w:
    if i in alpf:
        i = i + "c" + i
        print(i, end='')
    else:
        print(i, end='')
        continue;

    
