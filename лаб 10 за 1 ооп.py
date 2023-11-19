class Transport:#создание родительского класса транспорт
    def __init__(self, brand, max_speed, kind=None):#инициализация полей род. класса
        self.brand=brand
        self.max_speed=max_speed
        self.kind=kind
    def __str__(self):#возвращает информацию о транспорте
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'
class Car(Transport):#создание класса машина
    def __init__(self, brand, max_speed, mileage, gasoline_residue):#инициализация его полей
        super().__init__(brand, max_speed, kind='Car')#наследование род. класса
        self.mileage=mileage
        self.__gasoline_residue=gasoline_residue
    @property#прочтение поля
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_residue} км'
    @gasoline.setter#установка значения сеттерром
    def gasoline(self, value):
        if isinstance(value, int):#проверка является ли значение целым числом
            self.__gasoline_residue+=value#наращивание объёма, если да
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')#вывод информации об увеличении
        else:#если не является целым числом
            print('Ошибка заправки автомобиля')#вывод сообщения
class Boat(Transport):#создание дочернего класса лодка
    def __init__(self, brand, max_speed, owners_name):#инициализация его полей
        super().__init__(brand, max_speed, kind='Boat')#наследование род. класса
        self.owners_name=owners_name
    def __str__(self):#возвращает информацию о лодке
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
class Plane(Transport):#создание дочернего класса самолёт
    def __init__(self, brand, max_speed, capacity):#инициализация его полей
        super().__init__(brand, max_speed, kind='Plane')#наследование род. класса
        self.capacity=capacity
    def __str__(self):#возвращает информацию о самолёте
        return f'Самолёт марки {self.brand} вмещает в себя {self.capacity} людей'
    #создание объекта класса и вывод информации о нём
transport1=Transport('wolk', 145, 'машина')
print(transport1)
plane=Plane('wolk', 1200, 400)
print(plane)