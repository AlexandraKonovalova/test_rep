s = input('Enter a word: ')
vow = 'aeiouy'
con = 'bcdfghjklmnpqrstvwxz'
for i in range(0,len(s)):
    if s[0] in con:
        s = s[1:] + s[0]
print(s + "ay")
