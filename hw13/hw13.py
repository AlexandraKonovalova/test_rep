import os
import collections

#Получаем список расширений всех файлов

def ext():
    types = []
    for root, dirs, files in os.walk('.'):
        for fl in files:
            filename, file_extension = os.path.splitext(fl)
            types.append(file_extension)
    return types

#Делаем из них частотный словарь

def freq(d):
    counter = collections.Counter(d)
    counter = collections.Counter(counter).most_common(1)[0][0]
    return counter

###Находим самое частотное - это какой-то сложный вариант, я нашла .most_common()
## 
##def first(d):
##    main = sorted(d, key=d.get, reverse=True)
##    return 'Чаще всего встречаются: ' + '\"' + main[0] + \
##           '\":' + '\t' + str(d[main[0]])


def main():
    print('Самое частое разрешение: ', freq(ext()))

    
if __name__ == "__main__":
    main()
