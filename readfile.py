SYMBS = "1234567890,[]!\"'?.,*"

def readfile():
    s = []    
    with open("text.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.replace("  ", " ")
            line = line.lower()
            words = line.split()
            for el in words:
                s.append(el.strip(SYMBS))
    return s

readfile()

table = "\t".join(readfile())
with open("text1.txt", 'w', encoding='utf-8') as t:
    t.write(table)
