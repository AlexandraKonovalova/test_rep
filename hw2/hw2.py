s = input('Введите слово: ')
for i in range(len(s)-1,-1,-1):
    if s[i] == "з" or s[i] == "я":
        continue
    print(s[i])
