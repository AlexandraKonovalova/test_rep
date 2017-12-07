##def - объявляем функцию. Потом каждый раз нужно просто ее вызывать, вводя "say_hello"
def say_hello(username, age):
    if len(username) > 0:
        print('Hello, ' + username)
    else:
        print('No username given...')
    if age > 0:
        print('age ' + str(age))
say_hello("Vasya", 42)
say_hello("", 8)
##Чтобы установить ввод, придется вводить переменные


def say_hello(m, n):
    print(n)
    print(m)
say_hello(5, 6)
## Выводится 6, потом 5


n = 7
m = 8

def say_hello(m, n):
    print(n)
    print(m)
    
say_hello(5, 6)
## Переменные внутри функций не имеют отношения к переменным вне функций! Выводится 5, 6.
n = 7
m = 8

def say_hello(m, n):
    n = 9
    m = 10
    print(n)
    print(m)
say_hello(5, 6)

print(n)
print(m)
##Выведется 9, 10, 7, 8 (значение переменных не перезаписывается, считается, что они и переменные внутри функций - разные!!!)

n = 7
m = 8

def say_hello(m, n):
    x = m + n
##    print(n)
##    print(m)
    

say_hello(5, 6)
print(x)
##Выведет ошибку, потому что х внутри функции, считается необъявленным


n = 7
m = 8

def say_hello(m, n):
    x = m + n
##    print(n)
##    print(m)
    return x

y = say_hello(5, 6)

print(y)


##Если забыли написать return, то получается типа данных "NoneType".


def say_hello(n, m):
    x = n + m
    return x
def say_hello2(n, m):
    y = n - m
    return y
def main():
    n = int(input('Задайте значение первой переменной: '))
    m = int(input('Задайте значение второй переменной: '))
    x = say_hello(n, m)
    y = say_hello2(x, m) 
    print(y)
main()

def say_hello(n, m):
    return x
def say_hello2(n, m):
    return y
def main():
    n = int(input('Задайте значение первой переменной: '))
    m = int(input('Задайте значение второй переменной: '))
    x = say_hello(n, m)
    y = say_hello2(x, m) 
    print(y)
if __name__ == '__main__':
main()

