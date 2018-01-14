import random
SOFT = 'ьеюяёи'

def noun():
    with open("noun.txt", 'r', encoding='utf-8') as f:
        noun = []
        for line in f:
            noun.append(line.strip())
    return random.choice(noun)

def verb():
    with open("verb.txt", 'r', encoding='utf-8') as f:
        verb = []
        for line in f:
            verb.append(line.strip())
    return random.choice(verb)

def adv():
    with open("adv.txt", 'r', encoding='utf-8') as f:
        adv = []
        for line in f:
            adv.append(line.strip())
    return random.choice(adv)



def place():
    with open("noun.txt", 'r', encoding='utf-8') as f:
        place = []
        for line in f:
            place.append(line.strip())
        place = random.choice(place)
        if place[-1] in SOFT:
            place = place[:-1] + 'ю'
        elif place[-1] == 'а':
            place = place[:-1] + 'е'
        else:
            place = place + 'у'
    return place

def intens(adv):
    with open("intens.txt", 'r', encoding='utf-8') as f:
        intens = []
        for line in f:
            intens.append(line.strip())
    return random.choice(intens) + ' ' + adv()

def obj():
    with open("noun_inan.txt", 'r', encoding='utf-8') as f:
        obj = []
        for line in f:
            obj.append(line.strip())
        obj = random.choice(obj)
        if obj[-1] in SOFT:
            obj = obj[:-1] + 'я'
        elif obj[-1] == 'а':
            obj = obj[:-1] + 'у'
    return obj

def verb_tr():
    with open("verb_tr.txt", 'r', encoding='utf-8') as f:
        verb_tr = []
        for line in f:
            verb_tr.append(line.strip())
    return random.choice(verb_tr)


def pos1():
    return noun() + ' ' + intens(adv) + ' ' + verb_tr() + ' ' + obj()

def pos2():
    return noun() + ' ' + adv() + ' ' + verb() + ' ' +\
      'по' + ' ' + place()

##def sentence():
##    sent = random.choice([1, 2, 3, 4, 5])
##random.shuffle
print(pos1())
