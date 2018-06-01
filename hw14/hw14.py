import re
import collections

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& )("

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def sent(text):
    pattern = re.compile(r'[.|!|?|...|…|\n]') 
    sent = {i.lower().strip(): i.lower().split() for i in pattern.split(text) if i}
    return sent


def words(d):
    for v in d.values():
        for i in v:
            i = i.strip(SYMBS)
            print('{}_{}'.format(i, str(len(i))))

    

def main():
    return words(sent(read("text.txt")))
    

if __name__ == "__main__":
    print(main())
