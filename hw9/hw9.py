import re

SYMBS = "1234567890,—[]!\"'«»?.,;:*{}<>@#$%^&)("

def cleanfile(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        words = f.read().lower().split()
    return words

def search(text):
    forms = []
    for word in text:
        if re.match('программир((у(ю(сь)?|ют(ся)?|ешь(ся)?|\
ете(сь)?|ет(ся)?|ем(ся)?|й(те(сь)?)?|я(сь)?|))\
|ова(ть(ся)?)|л(ся|(а|о|и)(сь)?)|(ующ|овавш)\
(ий|его|ему|им|ем|ая|ей|ую|ее|ие|их|им|ими)(ся)?|овав|(уем|ованн)\
(ый|ая|ое|ого|ом(у)?|ым|ой|ую|ые|ых|ым(и)?))$', word) and word not in forms:
            forms.append(word.strip(SYMBS))
    return forms

def main(forms):
    print('Найдены следующие формы:')
    for word in forms:
        print(word)

if __name__ == "__main__":        
    print(main(search(cleanfile("textic.txt"))))
    
