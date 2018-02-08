def char():
    with open('all-seasons.csv', 'r', encoding="utf-8") as f:
        char = {}
##        rep = 
        for line in f:
            print(line)
            line = line.split(',')
            print(line)
            char[line[2]] = line[3]
    return char
print(char())


##def rep():
##    with open('all-seasons.csv', 'r', encoding="utf-8") as f:
##        rep = []
##        for line in f:
##            line = line.split(',')
##            rep.append(line[3])
##    return rep
##
##def comp(char, rep):
##    
##        
