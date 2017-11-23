n = 0
with open("text.txt", 'w', encoding='utf-8') as f:
    s = input('Введите слово: ')
    while s:
        n += 1
        s = s[n::1]
        f.write(s + '\n')
        s = input('Введите слово: ')
