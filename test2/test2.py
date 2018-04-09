import re
import collections

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.readlines()
    return text

def write(text):
    with open('number.txt', 'w', encoding='utf-8') as t:
        t.write(str(len(text)))

def dictionary(filename):
    word = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            r = re.search('<w lemma=".*" type="(.*)">', line)
            if r:
                word.append(r.group(1))
        dictionary = collections.Counter(word)
        return dictionary

def write_d(dictionary):
    keys = list(dictionary.keys())
    keys = '\n'.join(keys)
##    for k in dictionary:
##        table = 
    with open('keys.txt', 'w', encoding='utf-8') as t:
        t.write(keys)

def adj(dictionary):
    count = collections.Counter(dictionary)
    return count

def get_adj():
    adj = []
    with open('keys.txt', 'r', encoding='utf-8') as f:
        for line in f:
            r = re.search('(l.f.*)', line)
            if r:
                adj.append(r.group(1))
    return adj

def write_adj(d):
    table = []
    with open('adj.txt', 'w', encoding='utf-8') as t:
        for word in sorted(d, key=d.get, reverse=True):
            table.append(word + '\t' + str(d[word]))
        table = '\n'.join(table)
        t.write(table)

##3 номер не работает(
##def clean(filename):
##
##    with open(filename, 'r', encoding='utf-8') as f:
##        for line in f:
##            r = re.sub('<.+?>', '', line)
##            print(line)


def main():
    return write(read('text.xml')), write_d(dictionary('text.xml')), write_adj(adj(get_adj()))

if __name__ == "__main__":
    main()

##print(clean('text.xml'))

##dictionary('text.xml')
##write_d(dictionary('text.xml'))
####write_d(adj('text.xml'))
##write_adj(adj(get_adj()))
##write(read('text.xml'))
##clean('text.xml')
