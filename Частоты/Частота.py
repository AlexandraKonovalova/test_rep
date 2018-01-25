SYMBS = "1234567890,-—[]!–\"'«»?.,;*{}<>@#$%^& )("


def readfile():
    s = []    
    with open("Pushkin.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.lower()
            line = line.replace("  ", " ")
            words = line.split()
           
            for word in words:
                if word:
                    s.append(word.strip(SYMBS))
    return s


def add(words):

    d = {}
    
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


##def main():
##    with open('new.txt', 'w', encoding='utf-8') as t:
##        t.write(add(readfile()))
##    return t
##
##main()

def main(d):
    for word in sorted(d, key = d.get, reverse = True):
        print(word, '\t', d[word])
##    for k in d:
##        print(k, '\t', d[k])
            
print(main(add(readfile())))
