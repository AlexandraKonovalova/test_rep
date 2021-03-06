## Словари - структура данных, хранит в себе пары: ключ и значение
## К одному элементу привязаны какие-либо значения
## Key   --  Value
##  A           5
##  B           6
##  C           7
##
## 1) ключи не могут повторяться
## 2) переменная - любой тип данных
##    ключи - только неизменяемый тип данных

## Зададим пустой словарь
def main():
    d = {}

    ## Ключ - [], значение - =''
    d[1] = 'a'
    d['a'] = 1

    ## Вызвать по ключу 1 значение 
    s = d[1]

    ## Порядок добавления значения не сохраняется, в отличие от списков.
    ## Функция len() выводит кол-во пар ключ-значение

    for k in d:
        v = d[k]
        print(v)

if __name__ == "__main__":
    main()
