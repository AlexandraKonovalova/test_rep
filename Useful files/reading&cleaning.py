def readfile():
    s = []
    punct = ".,;:()\"\'!?"
    with open("text1.txt", 'r', encoding='utf-8') as f:
        for line in f:
##            line = line.strip()
##            line = line.replace("  ", " ")
##            for i in line:
##                if i in punct:
##                     line = line.replace(i, "")
##            line = line.lower()
##            words = line.split()
##            s.extend(words)
            words = line.split()
            for el in words:
                s.append(el.strip(punct))
    print(s)
readfile()
