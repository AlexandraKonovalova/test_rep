vow = "аеёиоуыэюя"
cons = "бвгджзклмнпрстфхцчшщ"
n_vow = 0
n_cons = 0
n_prep = 0
with open("C:/Users/student/Desktop/text.txt", "r", encoding="utf-8") as f:
    s = f.read()
    sent = s.split(". ")
    print(len(sent))


with open("C:/Users/student/Desktop/text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    strings = "".join(lines)
for letter in strings:
    if letter in vow:
        n_vow += 1
    if letter in cons:
        n_cons +=1
print("Количество гласных: ", n_vow, "Количество согласных: ", n_cons)
if " под " in strings:
    n_prep += 1
elif ". Под " in strings:
    n_prep += 1
print("Количество предлогов 'под': ", n_prep)
