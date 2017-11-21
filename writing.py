##n_words = 0
with open("text1.txt", 'r', encoding="utf-8") as f:
    with open("table.txt", 'w', encoding="utf-8") as t:
        for line in f:
            s = line.split()
            if len(s) > 0:
                t1 = len(s)
                t2 = s[0]
##                data = 
                print(t1, '\t', t2)
##                t.write(data)
            else:
                continue;

    
