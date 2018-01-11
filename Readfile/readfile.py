import random

SYMBS = "1234567890,—[]!\"'?.,;*{}<>@#$%^&)("
an = []

def readfile():
    s = []    
    with open("text.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.lower()
            words = line.split()
            line = line.replace("  ", " ")
            for el in words:
                s.append(el.strip(SYMBS))
    return s

def mix(string):
    string = list(string)
    random.shuffle(string)
    string = "".join(string)
    return string


with open("text1.csv", 'w', encoding='utf-8') as t:
    for line in readfile():
        an.append(line + "\t" + mix(line) + "\t" + mix(line) + "\t" + mix(line))
    t.write("\n".join(an))
