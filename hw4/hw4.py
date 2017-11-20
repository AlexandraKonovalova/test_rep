n_words_3 = 0
n_words_1 = 0
with open("text.txt", "r", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        for i in words:
            if len(i) == 3:
                n_words_3 += 1
            elif len(i) == 1:
                n_words_1 += 1;
if n_words_1 == 0:
    print("Нет слов длины 1")
elif n_words_3 == 0:
    print("Нет слов длины 3")
else:
    print("В тексте слов длины 3 в", n_words_3 / n_words_1, "раз больше, чем слов длины 1")
