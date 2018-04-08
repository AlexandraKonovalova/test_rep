import re

def page(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        page = f.read()
    return page

def shvili(page):
    r = re.findall('швили,.+?<', page)
    shvili = len(r)
    return shvili


def dze(page):
    r1 = re.findall('дзе,.+?<', page)
    dze = len(r1)
    return dze

def ia(page):
    r2 = re.findall('title="[А-Я].+?ия,.+?<', page)
    ia = len(r2)
    return ia

def count(shvili, dze):
    count = dze/shvili
    return count

def replace(page):
##    r = re.sub('швили|дзе',, page)
##    r = re.search('([А-Я].+? )([А-Я].+? )([А-Я].+?(швили|дзе))', page)
##    if r:
##        name = r.group(2)
##        if len(name) > 6:
##            print(name)
##    with open('result.html', 'w', encoding='utf-8') as t:
##        t.write(r)
##        print(r)
            
##            name = r.group(2)
##            if len(name) > 6:
##                print('yes')
    r = re.sub('([А-Я].+? )([А-Я]......+ )([А-Я].+?(швили|дзе))', r'\1Галактион \3', page)
    with open('result.html', 'w', encoding='utf-8') as t:
        t.write(r)
##        name = group(1)
##        if len(name) > 6:
##            r = re.sub('([А-Я].+? )([А-Я].+? )([А-Я].+?(швили|дзе)', r'Галактион \2\3', page)

def main():
    print('Людей на -дзе больше в: ', count(shvili(page('george.html')), dze(page('george.html'))), 'раз')
    print('Людей на -ия: ', ia(page('george.html')))
    return replace(page('george.html'))

if __name__ == "__main__":
    main()


