a={ '1.01.2017': 'Заметка 1',
    '5.03.2018': 'Заметка 2',
    '10.05.2019': 'Заметка 3',
    '15.07.2020': 'Заметка 4',
    '20.09.2021': 'Заметка 5',
    '25.11.2022': 'Заметка 6',
    '30.01.2023': 'Заметка 7'}
for key, value in a.items():
    print(key, value)
vibor_key= input('Введите ключ  ')
if vibor_key in a:
    print('Значение:', a[vibor_key])
else:
    print('Ключ не найден ')