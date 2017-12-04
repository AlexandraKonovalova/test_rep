s = []
for i in range(0,7):
    s.append(int(input('Введите число: ')))
with open('result.txt', 'w', encoding='utf-8') as f:
    for i in range(0,len(s)):
        if s[i] > 0:
            f.write("X"*s[i] + '\n')
        else:
            f.write('\n')
