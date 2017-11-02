alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
word = input("Введите слово: ")
n = 1
new_word = []
while word:
##    print(word)
    
    word_list = list(word)
    for i in word_list:
        for i2 in alf:
            if i == i2:
                for n,sym in enumerate(alf):
                    n = alf[i2]
            
                    new_word.append(alf[n])
                    n += 1
    result = "".join(new_word)
    print(result)
    word = input("Введите слово: ")
