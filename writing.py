n_line = 0
with open("text.txt", 'r', encoding="utf-8") as f:
    with open("table.txt", 'w', encoding="utf-8") as t:
        for line in f:
            s = line.split()
            if len(s) > 0:
                t1 = str(len(s))
                t2 = str(s[0])
                n_line += 1
            else:
                continue
            t.write(str(n_line) + '\t' + t1 + '\t' + t2 + '\n')


    
