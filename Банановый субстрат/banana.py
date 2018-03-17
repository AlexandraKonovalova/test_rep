##текст бьем на слова
##каждое слово проверяем на соответствие
##если подходит - с помощью групп извлекаем и показываем


import re

SYMBS = "1234567890,—[]!\"'«»?.,;*{}<>@#$%^&)("


def readfile():
    s = []    
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read().lower().split()
        for word in text:
            s.append(word.strip(SYMBS))
    return s

def main(text):
    for word in text:
        r = re.search('^[бвгджзйклмнпрстфхцчшщ]([аеёиоуыэюя])([бвгджзйклмнпрстфхцчшщ]\\1)+$', word)
        if r:
            string = r.group()
            print(string)

##def main():
##search(readfile())

if __name__ == "__main__":        
    main(readfile())
