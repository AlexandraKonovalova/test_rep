import re
import collections

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& )("

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def sent(text):
##    sent = re.split(r'[.!?] [А-Я]|[A-Z]', text)
    sent = [i.lower().strip(SYMBS) for i in re.split(r'[.!?]= [А-Я]|[A-Z]', text)]
    print(sent)

def main():
    return sent(read("text.txt"))


if __name__ == "__main__":
    print(main())
