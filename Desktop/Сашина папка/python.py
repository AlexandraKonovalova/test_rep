d = {}
str = input()
words = str.split(' ')
for i in words:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    print (i, '\t', d[i])
