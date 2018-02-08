def file():
    with open('81A.tab.txt', 'r', encoding="utf-8") as f:
        d = []
        for line in f:
            line = line.split('\t')
            d.append(line[3])
    return d


def order(file):
    d = {}
    for word in file:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def main(order(file())):
    for word in sorted(d, key = d.get, reverse = True):
        print(word, '\t', d[word])

if __name__=='__main__':
    main()
    
    
