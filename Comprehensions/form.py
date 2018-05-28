import re

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& )("

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def clean(text):
    text = text.strip().lower().split()
    words = [i.strip(SYMBS).lower() for i in text if len(i) > 0]
    return words

def form(s):
    i = 1
    for word in s:
        print('{}. {:>10}'.format(i, word))
        i += 1

def main():
    return (form(clean(read('text.txt'))))

if __name__ == "__main__":
    main()
