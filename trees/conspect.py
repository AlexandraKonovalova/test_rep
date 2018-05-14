import os

lst = os.listdir(path)

#Дерево каталогов
#Если внутри папки есть другие,
# root - string, какой путь(адрес) к той папке, к которой мы обращаемся
# dirs - только список папок, если нет папок - []
# files - список файлов, лежащих в той папке, в которой мы сейчас находимся

# .endswith('') / .startswith('')
for root, dirs, files in os.walk(path):
    for fl in files:
        if not fl.endswith('.txt'):
            continue
        f = open(root + os.sep + fl)

#сколько имен каталогов в дереве каталогов с 'r'  в названии,
        #сколько файлов с названием 'd', если 'd'  в папке с 'r', вывести
        
