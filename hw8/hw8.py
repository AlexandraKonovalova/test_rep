import random

def prompt(filename):
    d = {}
    with open(filename, 'r', encoding='utf-8') as f:
        game = ''
        for line in f:
            if line == 'Word\tPrompt\n':
                continue
            if game == '':
                word, prompt = line.strip().split('\t', maxsplit = 1)
                d[word] = prompt
    return d

## Следующая функция выглядит кошмарно длинной,
## но по сути - это просто из-за переборов разных вариантов ввода

def lets_play(dictionary):
    print('Добро пожаловать в игру!\nВам нужно угадывать слова по подсказке.\n\
У вас столько попыток, сколько букв в подсказке.\nЕсли не можете отгадать слово, введите "я сдаюсь"')
    wish = input('Хотите сыграть? Тогда наберите "да": ')
    while wish.lower() == 'да':
        tries = 0
        key = random.choice(list(dictionary))
        print('Подсказка: ', dictionary[key].capitalize(), ' ...')
        attempt = input('Ваша попытка: ')
        while attempt.lower() != key.lower() and attempt.lower() != 'я сдаюсь'\
              and tries < len(dictionary[key])-1:
            print('Не совсем... Попробуйте еще раз! Осталось попыток: ', \
              len(dictionary[key])-1-tries)
            attempt = input('Ваша попытка: ')
            tries += 1
        if tries == len(dictionary[key])-1:
            print("Все, попытки закончились. А слово простое: ", key)
            wish = input('Хотите сыграть? Тогда наберите "да": ')
        if attempt.lower() == key:
            print("Правильно!")
            wish = input('Хотите сыграть? Тогда наберите "да": ')
        if attempt.lower() == 'я сдаюсь':
            print('Так и быть. Это простое слово: ', key)
            wish = input('Хотите сыграть? Тогда наберите "да": ')
        


def main():
    print(lets_play(prompt("prompt.csv")))

if __name__ == "__main__":
    main()
