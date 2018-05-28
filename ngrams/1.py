import collections
import re

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& )("

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

##def clean(t):
##    text = re.sub('\,—[]!­\"\'«»\?\.,;:|/+*{}<>@#$%^& )([0-9]', '', t)
##    return text

def clean(text):
    words = []
    text = text.strip().lower().split()
    for word in text:
        if word:
            words.append(word.strip(SYMBS))
    return words

def ngrams(words):
    n = int(input('Введите число слов в n-грамме: '))
    d = {}
    for i in range(len(words)):
        gr = ' '.join(words[i+1:n+i])
        if gr in d and len(gr) >= 1:
            d[gr] += 1
        else:
            d[gr] = 1
    return d

def write(d):
    table = []
    with open('result.tsv', 'w', encoding='utf-8') as t:
        for word in sorted(d, key=d.get, reverse=True):
            table.append(word + '\t' + str(d[word]))
        table = '\n'.join(table)
        t.write(table)

def main():
    return write(ngrams(clean(read('text.txt'))))


if __name__ == "__main__":
    print(main())

print(clean(read('text.txt')))
