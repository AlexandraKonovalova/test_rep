def readfile():
    s = []
##    file = input('Введите полное имя файла: ')
    with open("text.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace("  ", " ")
            line = line.strip()
            words = line.split()
            for i in words:
                s.append(i)
        return s
readfile()
