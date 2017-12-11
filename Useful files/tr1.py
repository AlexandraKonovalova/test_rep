alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэю"
w = input("слово: ")
for i in range(1, len(w), 2):
    if w[i] != "а" and w[i] != "к":
        print(w[i])
