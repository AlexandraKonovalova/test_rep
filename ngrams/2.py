def words():
    words = ['i', 'love', 'you', 'love', 'you']
    return words
def ngrams(words):
    n = int(input('Введите число слов в n-грамме: '))
    d = {}
    for i in words:
        if words[i:n-i] in d:
            d[i:n-i] += 1
        else:
            d[i:n-i] = 1
    return d

print(ngrams(words))
