def readfile():
    s = []
    with open("text.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.replace("  ", " ")
            line = line.lower()
            words = line.split()
            s.extend(words)
    return s
readfile()
