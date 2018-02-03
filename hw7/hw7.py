SYMBS = "1234567890,—[]!­\"'«»?.,;:|/+*{}<>@#$%^& )("

def cleanfile(file_name):
    s = []    
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.lower()
            line = line.replace("  ", " ")
            words = line.split()
            for word in words:
                if word:
                    s.append(word.strip(SYMBS))
    return s

def search(text):
    d = {}
    for word in text:
        if len(word) > 4:
            if word[-4:] == 'hood':
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
    return d

def freq(d):
    if d:
        values = list(d.values())
        print('Минимальную частотность имеют существительные: ')
        for key in sorted(d, key=d.get):
            if d[key] == min(values):
                print(key)

def length(d):
    keys = list(d.keys())
    if len(keys) > 0:
        print('Существительных с суффиксом -hood: ' + str(len(keys)))
    else:
        print('В тексте нет существительных с суффиксом -hood.')

def deriv(d):
    if d:
        print('Существительные образованы от слов: ')
        for key in sorted(d, key = d.get, reverse = True):
            print(key[:-4])

def main(fun):
    return length(fun), freq(fun), deriv(fun), 

    
if __name__ == "__main__":        
    main(search(cleanfile(input('Введите имя файла: '))))
