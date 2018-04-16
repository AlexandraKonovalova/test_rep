import os
import shutil

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& )("

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def clean(text):
    words = []
    text = text.strip().lower().split()
    for word in text:
        if word:
            words.append(word.strip(SYMBS))
    return words

def cut(words):
##    with open('')
    
    if len(words) > 2000:
        num = len(words) // 2000
        for i in range(num):
            text = ' '.join(words[((i-1)*2000):(i*2000)])
            name = 'text' + str(i) + '.txt'
##        with open('te, ''.txt', 'x'):
##            pass
            os.mkdir(str(i))
            with open(name, 'w', encoding='utf-8') as t:
                t.write(text)
            shutil.move(name, str(i))

cut(clean(read('text.txt')))
