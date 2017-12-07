def say_hello(n, m):
    return n + m
def say_hello2(n, m):
    return n - m
def main():
    n = int(input('Задайте значение первой переменной: '))
    m = int(input('Задайте значение второй переменной: '))
    x = say_hello(n, m)
    y = say_hello2(x, m) 
    print(y)
if __name__ == '__main__':
    main()
