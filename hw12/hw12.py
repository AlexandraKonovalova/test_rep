import os
import re


#Вроде бы к кириллическим символам знаки препинания и цифры не относятся?

def folder():
    folders = []
    for folder in os.listdir():
        if os.path.isdir(folder):
            dirpath, filename = os.path.split(folder)
            r = re.search('[A-Z]|[a-z]|[0-9]|[,—\[\]↑№!\"\'«»?.,;:-|/+*{}<>@#$%-^&()]', filename)
            if not r:
                folders.append(filename)
    return folders
            
def num_dir(folders):
    print(int(len(folders)))

#Вообще папки с одинаковым названием не создаются, но на всякий случай делаю попытку этого избежать

def no_repeat(folders):
    check = []
    for i in folders:
        if i not in check:
            check.append(i)
            print('Есть такая папка: ', i)
            
def main():
    return num_dir(folder()), no_repeat(folder())

if __name__ == "__main__":
    print('Всего папок: ', end='')
    main()

