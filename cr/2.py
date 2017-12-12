with open("Ozhegov.txt", 'r', encoding='utf-8') as f:
    w = input("Введите слово: ")
    for line in f:
        line = line.split("|")
        if line[0] == w:
            line = " - ".join(line)
            print(line)
        else:
            continue
    w = input("Введите слово: ")
