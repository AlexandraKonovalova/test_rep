import re

SYMBS = "1234567890,—[]!\"'«»?.,;*{}<>@#$%^&)("


def readfile():
    s = []    
    with open('mexico.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        sentences = text.split(". ")
    return sentences

def search(text):
    for word in text:
        r = re.search('([0-9]+)(-е$|х$| г(\.|г\.|од(.+)?))', word)
        if r:
            string = r.group(1)
            print(string)
search(readfile())
