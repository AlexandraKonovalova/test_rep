word = input('Введите слово: ')
while word:
    print(word)
    for i in range(0, len(word)-1):
        new_word = []
        new_word.append(word[1:len(word):1])
        s1 = word[:1]
        new_word.append(s1)
        s2 = "".join(new_word)
        print(s2)
        word = s2
    word = input("Введите слово: ")
