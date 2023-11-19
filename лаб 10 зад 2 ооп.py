class Cars:#создание родительского класса
    def __init__(self, brand, year, price, configuration, country, sale_date, buyer_name):#инициализация полей род. класса
        self.brand = brand
        self.year = year
        self.price = price
        self.configuration = configuration
        self.country = country
        self.sale_date = sale_date
        self.buyer_name = buyer_name
    def __str__(self):#возвращает информацию о транспорте
        return f'Марка: {self.brand}\nГод выпуска: {self.year}\nЦена: {self.price}\n' \
               f'Комплектация: {self.configuration}\nСтрана: {self.country}\n' \
               f'Дата продажи: {self.sale_date}\nИмя покупателя: {self.buyer_name}'
class UsedCars(Cars):#создание дочернего класса подержанные авто
    def __init__(self, brand, year, price, configuration, country, sale_date, buyer_name, preservation_degree, owner_name, mileage):#инициализация его полей
        super().__init__(brand, year, price, configuration, country, sale_date, buyer_name)#наследование род. класса
        self.preservation_degree = preservation_degree
        self.owner_name = owner_name
        self.mileage = mileage
    def __str__(self):#вовращает информацию о подержанном авто
        return f'Марка: {self.brand}\nГод выпуска: {self.year}\nЦена: {self.price}\n' \
               f'Комплектация: {self.configuration}\nСтрана: {self.country}\n' \
               f'Дата продажи: {self.sale_date}\nИмя покупателя: {self.buyer_name}\n' \
               f'Сепень сохранности: {self.preservation_degree}\nИмя владельца: {self.owner_name}\nПробег: {self.mileage}'
class SportsCars(Cars):#создание дочернего класса спорткар
    def __init__(self, brand, year, price, configuration, country, sale_date, buyer_name, seconds_to_speed, engine_volume, horsepower):#инициализация его полей
        super().__init__(brand, year, price, configuration, country, sale_date, buyer_name)#наследование род. класса
        self.seconds_to_speed = seconds_to_speed
        self.engine_volume = engine_volume
        self.horsepower = horsepower
    def __str__(self):#возвращет информацию о спорткаре
        return f'Марка: {self.brand}\nГод выпуска: {self.year}\nЦена: {self.price}\n' \
               f'Комплектация: {self.configuration}\nСтрана: {self.country}\n' \
               f'Дата продажи: {self.sale_date}\nИмя покупателя: {self.buyer_name}\n' \
               f'Секунд от 0 до 100: {self.seconds_to_speed}\nОбъём двигателя: {self.engine_volume}\nМощность: {self.horsepower}'
class SpecialEquipment(Cars):#создание дочернего класса спецтехника
    def __init__(self, brand, year, price, configuration, country, sale_date, buyer_name, type_of_equipment, weight, dimensions):#инициализация его полей
        super().__init__(brand, year, price, configuration, country, sale_date, buyer_name)#наследование род. класса
        self.type_of_equipment = type_of_equipment
        self.weight = weight
        self.dimensions = dimensions
    def __str__(self):#возвращает информацию о спецтехнике
        return f'Марка: {self.brand}\nГод выпуска: {self.year}\nЦена: {self.price}\n' \
               f'Комплектация: {self.configuration}\nСтрана: {self.country}\n' \
               f'Дата продажи: {self.sale_date}\nИмя покупателя: {self.buyer_name}\n' \
               f'Вид техники: {self.type_of_equipment}\nВес: {self.weight}\nГабаритные азмеры: {self.dimensions}'
    #создание объекта класса
car1=SportsCars('mazda', 2011, 200000, 'ac 100', 'Japan', '12:10:21', 'Josh', 3.4, 8.0, 2400)
print(car1)#вывод информации об объекте