m = int(input('Введите ваш вес в кг: '))
h = int(input('Введите ваш рост в см: '))
bmi = m/((h/100)**2)
if bmi <= 16:
    print('Выраженный дефицит массы тела')
elif 16 < bmi < 18.5:
    print('Недостаточная (дефицит) масса тела')
elif 18.5 <= bmi <= 24.99:
    print('Норма')
elif 25 <= bmi < 30:
    print('Избыточная масса тела (предожирение)')
elif 30 <= bmi < 35:
    print('Ожирение первой степени')
elif 35 <= bmi < 40:
    print('Ожирение второй степени')
elif 40 <= bmi:
    print('Ожирение третьей степени (мордобидное)')
