import re

SYMBS = "1234567890,—[]↑№-!\"'«»?.,;:|/+*{}<>@#$%^& )("
ALF = "absdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def no_tags(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        plain_text = re.sub('<.+?>', '', text)
        plain_text = re.sub('&.+?;', '', plain_text)
##        newtext = re.sub('[A-Z],—[]!\"\'«»?.,;:|/+*{}<>@#$%^& )([a-z][0-9]', '', plain_text)
        with open('goodtext.txt', 'w', encoding='utf-8') as t:
            t.write(plain_text)
    return t

def cleanfile():
    s = []    
    with open('goodtext.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().lower().split()
            for word in line:
                for letter in word:
                    if letter in ALF:
                        word = ''
                if word:
                    s.append(word.strip(SYMBS))
    return s

def dictionary(s):
    d = {}    
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def array(d):
    table = []
    for word in sorted(d, key = d.get, reverse = True):
        table.append(word + '\t' + str(d[word]))
        array = '\n'.join(table)
    with open('result.txt', 'w', encoding='utf-8') as t:
        t.write(array)
##    with open('result.txt', 'w', encoding='utf-8') as t:
##        table = []
##        for word in sorted(d, key = d.get, reverse = True):
##            table.append(word + '\t' + str(d[word])
##        t.write('\n'.join(table))

##    return t

def main():
    return no_tags('war.html'), array(dictionary(cleanfile()))

if __name__ == "__main__":        
    main()
