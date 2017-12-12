n_lines = 0
no = 0
with open("Ozhegov.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split("|")
        n_lines += 1
        for i in line:
            if i == "":
                no += 1
        if len(line[0]) >= 20:
            line = " | ".join(line)
            print(line)
    n_lines = n_lines - no
    print("Antonims: ", n_lines)
        


