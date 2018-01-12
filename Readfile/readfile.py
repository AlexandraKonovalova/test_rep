import random

SYMBS = "1234567890,—[]!\"'?.,;*{}<>@#$%^&)("


def readfile():
    s = []    
    with open("text.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.lower()
            words = line.split()
            line = line.replace("  ", " ")
            for word in words:
                s.append(word.strip(SYMBS))
    return s

def mix(string):
    string = list(string)
    random.shuffle(string)
    string = "".join(string)
    return string

def main():
    with open("text1.csv", 'w', encoding='utf-8') as t:
        an = []
        for word in readfile():
            an.append(word + "\t" + mix(word) + "\t" + mix(word) + "\t" + mix(word))
        t.write("\n".join(an))
    return t

main()
