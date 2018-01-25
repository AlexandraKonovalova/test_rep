d = {'mouse': 34, 'cat': 44, 'elephant': 98}
def alf():
    for k in sorted(d):
        print(k, d[k])

## Поиск по значению
def search():
    for word in sorted(d, key = d.get, reverse = True):
        print(d[word])

def all_keys():
    return d.keys()
print(all_keys())
