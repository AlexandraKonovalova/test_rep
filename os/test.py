import os
import shutil
import collections

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%–-^& )("

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def clean(text):
    words = []
    text = text.strip().lower().split()
    for word in text:
        if word != '':
            words.append(word.strip(SYMBS))
    return words

def cut(words):
    if len(words) > 2000:
        for i in range(len(words) // 2000):
            text = '\n'.join(words[((i-1)*2000):(i*2000)])
            if i == (len(words) // 2000) + 1:
                text = '\n'.join(words[((i-1)*2000):])
            path = './' + str(i)
            if os.path.exists(path):
                shutil.rmtree(path)
            os.mkdir(str(i))
            with open('text' + str(i) + '.txt', 'w', encoding='utf-8') as t:
                t.write(text)
            shutil.move('text' + str(i) + '.txt', str(i))
    return len(words) // 2000

def dictionary(n):
    file_list = os.listdir()
    for folder in sorted(file_list):
        if os.path.isdir(folder):
            for filename in os.listdir(folder):
                filepath = os.path.join(folder, filename)
                with open(filepath, encoding='utf-8') as f:
                    words = f.read().split('\n')
                counter = collections.Counter(words)
                with open('Dictionary' + folder + '.txt', 'w', encoding='utf-8') as t:
                    for word in sorted(counter, key=counter.get, reverse=True):
                        table = []
                        table.append(word + '\t' + str(counter[word]) + '\n')
                        table = '\n'.join(table)
                        t.write(table)
                shutil.move('Dictionary' + folder + '.txt', str(folder))
            
                    
def main():
    return cut(clean(read('Pushkin.txt'))), dictionary(cut(clean(read('Pushkin.txt'))))
  
if __name__ == "__main__":
    main()
