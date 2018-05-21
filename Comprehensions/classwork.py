import re

def lst():
    words = ['Анна', 'Brother', 'Moscow', 'Калуга', 'MOSЛИНГ']
    new_lst = [i.lower() for i in words if re.search('^[a-zA-Z]+$', i)]
    return new_lst

def dict(words):
    d1 = {k : v for k, v in enumerate(words)}
    return d1
print(dict(lst()))

t = '{:.2f}'.format(pi)
print(t)
