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
    with open("noun_inan.txt", 'r', encoding='utf-8') as f:
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

def verb_pf():
    with open("verb_pf.txt", 'r', encoding='utf-8') as f:
        verb_pf = []
        for line in f:
            verb_pf.append(line.strip())
    a = noun()
    b = random.choice(verb_pf)
    if a[-1] == 'а' or a[-1] == 'я':
        if b[-2:] == 'ся':
            return a + ' ' + b[:-2] + 'ась'
        else:
            return a + ' ' + b + 'а'
    elif a[-1] == 'о' or a[-1] == 'е':
        if b[-2:] == 'ся':
            return a + ' ' + b[:-2] + 'ось'
        else:
            return a + ' ' + b + 'о'
    else:
        return a + ' ' + random.choice(verb_pf)

def verb_imp():
    with open("verb_imp.txt", 'r', encoding='utf-8') as f:
        verb_imp = []
        for line in f:
            verb_imp.append(line.strip())
    return random.choice(verb_imp)

def conj():
    with open("conj.txt", 'r', encoding='utf-8') as f:
        conj = []
        for line in f:
            conj.append(line.strip())
    return random.choice(conj)

def que_word():
     with open("que.txt", 'r', encoding='utf-8') as f:
        que = []
        for line in f:
            que.append(line.strip())
     return random.choice(que)

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

def cond1():
    return verb_pf() + ' ' + 'бы' + ', ' + conj() +\
           ' ' + verb_pf()
def cond2():
    return verb_pf() + ' ' + 'бы' + ' ' + 'по' + ' ' + place() + ', ' + conj() +\
           ' ' + verb_pf() + ' ' + intens(adv)
def cond3():
    return conj() + ' ' + verb_pf() + ', ' + verb_pf() + ' ' + 'бы' + ' ' + intens(adv)

def cond4():
    return verb_imp() + ' ' + noun() + ' ' + 'по' + ' ' + place() + ', ' +\
           verb_pf() + ' ' + 'бы'

def cond_sent():
    sent = random.choice([1, 2, 3, 4])
    if sent == 1:
        return cond1()
    elif sent == 2:
        return cond2()
    elif sent == 3:
        return cond3()
    else:
        return cond4()

def imp1():
    return noun() + ', ' + verb_imp() + ' ' + verb_inf() + '!'

def imp2():
    return verb_imp() + ' ' + verb_inf() + ' ' + adv() + '!'

def imp3():
    return verb_imp() + ', ' + 'пожалуйста, ' + 'по' + ' ' + place()

def imp4():
    return 'когда' + ' ' + noun() + ' ' + verb() + ', ' + verb_imp()

def imp_sent():
    sent = random.choice([1, 2, 3, 4])
    if sent == 1:
        return imp1()
    elif sent == 2:
        return imp2()
    elif sent == 3:
        return imp3()
    else:
        return imp4()

def que1():
    return noun() + ' ' + verb() + ' ' + 'по'  + ' ' + place()  + '?'

def que2():
    return noun() + ' ' + verb_tr() + ' ' + obj() + '?'

def que3():
    return que_word() + ' ' + noun() + ' ' + verb_tr() + ' ' + obj() + '?'

def que4():
    return que_word() + ' ' + verb_pf() + '?'

def que_sent():
    sent = random.choice([1, 2, 3, 4])
    if sent == 1:
        return que1()
    elif sent == 2:
        return que2()
    elif sent == 3:
        return que3()
    else:
        return que4()

def main():                        
    text = []
    text.append(pos_sent())
    text.append(neg_sent())
    text.append(cond_sent())
    text.append(imp_sent())
    text.append(que_sent())
    random.shuffle(text)
    for i in text:
        i = i.capitalize()
        if i[-1] == '!' or i[-1] == '?':
            print(i, end = ' ')
        else:
            print(i, end = '. ')
main()

