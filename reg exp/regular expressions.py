import re

##SYMBS = "1234567890,—[]!\"'«»?.,;*{}<>@#$%^&)("

def readfile():
    s = []    
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        sentences = text.split(". ")
    return sentences
##        for line in f:
##            line = line.strip()
##            line = line.lower()
##            
##            line = line.replace("  ", " ")
##            for sent in sentences:
##                s.append(sent)
##    return s

def search(text):
    for s in text:
        if re.search('[0-9]+(-| г)', s):
##        if re.search('[0-9]+(-| г(\.|г\.|од(.+)?))', s):
            print(s, '###')

search(readfile())
