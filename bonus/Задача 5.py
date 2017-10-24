alpf = "bcdfghjklmnpqrstvwxz"
w = input('Please, enter a word in English: ')
for i in w:
    if i in alpf:
        i = i + "aig"
        print(i, end='')
    else:
        print(i, end='')
        continue;

    
