import random
SOFT = 'ьеюяёи'

def noun():
    with open("noun.txt", 'r', encoding='utf-8') as f:
        noun = []
        for line in f:
            noun.append(line.strip())
    return random.choice(noun)

def verb():
    with open("verb_mov.txt", 'r', encoding='utf-8') as f:
        verb_mov = []
        for line in f:
            verb_mov.append(line.strip())
    return random.choice(verb_mov)

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

def verb_able():
    with open("verb_able.txt", 'r', encoding='utf-8') as f:
        verb_able = []
        for line in f:
            verb_able.append(line.strip())
    return random.choice(verb_able)

def verb_inf():
    with open("verb_inf.txt", 'r', encoding='utf-8') as f:
        verb_inf = []
        for line in f:
            verb_inf.append(line.strip())
    return random.choice(verb_inf)

def pos1():
    return noun() + ' ' + intens(adv) + ' ' + verb_tr() + ' ' + obj()

def pos2():
    return noun() + ' ' + adv() + ' ' + verb() + ' ' + 'по' + ' ' + place()

def pos3():
    return noun() + ' ' + verb_able() + ' ' + verb_inf() + ' ' + intens(adv)

def pos4():
    return 'По' + ' ' + place() + ' ' + noun() + ' ' + verb_able() +\
           ' ' + verb_inf() + ' ' + intens(adv)

def pos_sent():
    sent = random.choice([1, 2, 3, 4])
    if sent == 1:
        return pos1()
    elif sent == 2:
        return pos2()
    elif sent == 3:
        return pos3()
    elif sent == 4:
        return pos4()


def neg1():
    return noun() + ' ' + 'не' + ' ' +\
           verb_able() + ' ' + verb_inf() + ' ' + intens(adv)
def neg2():
    return noun() + ' ' + 'не' + ' ' +  verb() + ' ' +\
      'по' + ' ' + place()

def neg3():
    return noun() + ' ' + 'не' + ' ' + verb_able() + ' ' + verb_inf()

def neg4():
    return noun() + ' ' + 'не' + ' ' + verb_tr() + ' ' + obj()

def neg_sent():
    sent = random.choice([1, 2, 3, 4])
    if sent == 1:
        return neg1()
    elif sent == 2:
        return neg2()
    elif sent == 3:
        return neg3()
    else:
        return neg4()
    
text = []
text.append(pos_sent())
text.append(neg_sent())
random.shuffle(text)
for i in text:
    i = i.capitalize()
    print(i, end='. ')
