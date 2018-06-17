import re
import collections

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& )("

## Эти общие, используются везде
def text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.readlines()
    return text

        
def bare_text(text):
    for i, line in enumerate(text):
        if re.search('<body', line):
            text = text[i:]
    bare_text = [re.sub('\t|<.+?>', '', line) for line in text]
    bare_text = ''.join(bare_text)
    return bare_text

##Первое задание
def length(bare_text):
    length = [len(word.lower().strip(SYMBS)) for word in bare_text.split()]
    average = round((sum(length) / len(length)), 2)
    return average

## Второе задание
def freq(bare_text):
    lst = [word.lower().strip(SYMBS) for word in bare_text.split()]
    counter = collections.Counter(lst)
    return counter

def print_freq(eng, cham):
    for i in range(10):
        a = collections.Counter(eng).most_common(10)[i][0]
        b = collections.Counter(cham).most_common(10)[i][0]
        print('{} : {}'.format(b, a))

## А вот это третье - и я не совсем понимаю в чем проблема.
##        Почему он выдает какую-то жесть, а не нормальный словарь?
##        То есть я понимаю, что много наверчено, но в закомменченном коде он почему-то выдает словарь из последних строк только
def rel(eng, cham):
##    sent_cham = {}
##    i = 0
##    for line in cham.split('\n'):
##         if len(line) > 0:
##            sent_cham[i] = len(line.split())
##            i += 1
##            if i >= 100:
##                break
##    sent_eng = {}
##    for line in eng.split('\n'):
##         if len(line) > 0:
##            sent_eng[i] = len(line.split())
##            i += 1
##            if i >= 100:
##                break
##    print(sent_eng)
    sent = {(len(line.split()) for line in cham.split('\n') if len(line) > 0):\
            (len(line.split()) for line in eng.split('\n') if len(line) > 0) for i in range(100)}
    print(sent)

rel(bare_text(text('English.xml')), bare_text(text('Chamorro-PART.xml')))


#Это были вспомогательные, не нужно смотреть


##def show_text():
##    with open('bare_text.txt', 'w', encoding='utf-8') as t:
##        t.write(bare_text(text('English.xml')))


##def write(d):
##    table = []
##    with open('result.txt', 'w', encoding='utf-8') as t:
##        for word in d:
####        for word in sorted(d, key=d.get, reverse=True):
##            table.append(word + '\t' + str(d[word]))
##        table = '\n'.join(table)
##        t.write(table)

def main():
    return length(bare_text(text('Chamorro-PART.xml')))

##show_text()
if __name__ == "__main__":
    print(main())
