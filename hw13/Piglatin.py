con = 'bcdfghjklmnzpqrstvwxwz'
vow = 'aeiouy'
s = ''
n = 0
m = ''
while 1:
    w = input('Please, enter a word in Roman alphabet: ')
    for i in w:
        if w[0] in con:
            s += w[0];
        else:
            s += w
    print(s)
