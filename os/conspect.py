import os


#Достать в виде списка список всех файлов и папок в директории
lst = os.listdir()
print(type(lst))

lst = os.listdir('C:/User')

os.path.join(name, file) #для борьбы с разными слэшами

lst = os.listdir(dir1 + os.sep + dir2)

for fn in lst:
    if os.psth.isfile(fn):
        f = open(fn)

import shutil

shutil.move(source, destination)
shutil.copy(source, destination)
shutil.remove() #???
shutil.rmtree() #стирает папку со всеми вложениями
