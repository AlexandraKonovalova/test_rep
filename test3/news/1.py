import re
import collections
import os

##"doc_id", "title", "author", "created", "topic", "tagging"


##Первое задание

def docid():
    docid = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.search('content="(.+?)" name="docid"', line)
                if r:
                    docid.append(r.group(1))
    return docid

def title():
    title = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.search('<title>(.+?)</', line)
                if r:
                    title.append(r.group(1))
    return title
        
def author():
    author = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.search('content="(.+?)" name="author"', line)
                if r:
                    author.append(r.group(1))
    return author

def created():
    created = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.search('content="(.+?)" name="topic"', line)
                if r:
                    created.append(r.group(1))
    return created

def topic():
    topic = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.search('content="(.+?)" name="created"', line)
                if r:
                    topic.append(r.group(1))
    return topic

def tag():
    tag = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.search('content="(.+?)" name="tagging"', line)
                if r:
                    tag.append(r.group(1))
    return tag

def table(docid, title, author, created, topic, tag):
    with open('table.csv', 'w', encoding='utf-8') as t:
        table = []
        table.append('doc.id' + '\t' + 'title' + '\t' + 'author' + '\t' + 'created' + '\t' + 'topic' + '\t' + 'tag')
        for i in range(15):
            table.append(docid[i] + '\t' + title[i] + '\t' + author[i] + '\t' + created[i] + '\t' + topic[i] + '\t' + tag[i])
        table = '\n'.join(table)
        t.write(table)

##Второе задание
def abb():
    abb = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.search('lex="([А-Я]+)"', line)
                if r:
                    abb.append(r.group(1))
    return abb

def counter(abb):
    counter = collections.Counter(abb)
    return counter

def table1(d):
    table = []
    with open('abbs.csv', 'w', encoding='utf-8') as t:
        for word in sorted(d, key=d.get, reverse=True):
            table.append(word + '\t' + str(d[word]))
        table = '\n'.join(table)
        t.write(table)

##  из-за первого это не успела написать, но нужно создать словарь с предложениями и искать биграммы как в коде, но по элементам из словаря. Потом из выводить
def noun():
    noun = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            text = f.readlines()
##            text = {}
            for i, line in enumerate(text):
                r = re.search('lex="(.+)" .+S', line)
                if r:
                    d = re.search('lex="(.+)" .+gen', text[i+1])
                    if d:
                        noun.append(r.group(1) + ' ' + d.group(1))
                        
    return noun

##def grams():
    
    
def main():
    return table(docid(), title(), author(), created(), topic(), tag()), \
           table1(counter(abb()))

##по крайней мере это выводит биграммы
print(noun())
##print(abb())
##print(docid())
##print(title())
##print(author())
##print(created())
##print(topic())
##print(tag())

if __name__ == "__main__":
    main()
