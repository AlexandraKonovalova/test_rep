##text2 = re.sub('([^оа])(р|л)(о|а)', '\1\3\2\3', text1)
import re

SYMBS = "1234567890,—[]!­\"'«»?.,;:|/+*{}<>@#$%^& )("

def no_tags(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        plain_text = re.sub('<.+?>', '', text)
        plain_text = re.sub('&.+?;', '', plain_text)
        with open('goodtext.txt', 'w', encoding='utf-8') as t:
            t.write(plain_text)

def dict(no_tags):
    d = {}
    with open('goodtext.txt', 'r', encoding='utf-8') as f:
        words = f.read().lower().split()
        for word in words:
            word = re.sub('[A-Z],—[]!­\"\'«»?.,;:|/+*{}<>@#$%^& )([a-z][0-9]', '', word):
                
        with open('goodtext.txt', 'w', encoding='utf-8') as t:
            t.write(words)

def main():
    return no_tags('war.html')

if __name__ == "__main__":        
    print(main())
