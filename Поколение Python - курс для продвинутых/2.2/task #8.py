timur, ruslan = input(), input()

graf = {'ножницы' : ['бумага', 'ящерица'],
        'бумага' : ['камень', 'Спок'],
        'камень' : ['ножницы', 'ящерица'],
        'ящерица' : ['Спок', 'бумага'],
        'Спок' : ['ножницы', 'камень']}

if ruslan in graf[timur]:
    print('Тимур')
elif timur in graf[ruslan]:
    print('Руслан')
elif ruslan == timur:
    print('ничья')
