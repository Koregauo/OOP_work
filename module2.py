class Product:
    """
    Класс, представляющий информацию о товаре.

    Атрибуты класса:
    - name(str): наименование товара.
    - manufacturer(str): производитель товара.
    - price(float): цена товара.
    - life(int): срок хранения товара в днях.
    - val(int): количество товара.

    Методы класса:
    - print_info(): выводит информацию о товаре.
    """

    def __init__(self, name, manufacturer, price, life, val):#инициализация
        """
        Инициализация экземпляра класса.

        Параметры:
        - name(str): наименование товара.
        - manufacturer(str): производитель товара.
        - price(float): цена товара.
        - life(int): срок хранения товара в днях.
        - val(int): количество товара.
        """
        self.name=name
        self.manufacturer=manufacturer
        self.price=price
        self.life=life
        self.val=val

    def print_info(self):#создание функции по выводу информации
        """
        Выводит информацию о товаре.
        """
        print(f'Наименование: {self.name}')
        print(f'Производитель: {self.manufacturer}')
        print(f'Цена: {self.price}')
        print(f'Срок хранения: {self.life} (дней)')
        print(f'Количество: {self.val}')

# Создание массива объектов класса Product
products = [
    Product('Молоко', 'Хуторок', 58.5, 7, 10),
    Product('Хлеб', 'Хлебный рай', 25.3, 3, 20),
    Product('Яблоки', 'Румянь', 85.1, 10, 15),
    Product('Колбаса', 'Мясной рай', 134.25, 5, 5),
    Product('Сок', 'Фабрика соков', 70.0, 14, 12)]

# Вывод списка товаров, срок хранения которых больше заданного
extra_date=7  # заданный срок хранения
#проверка на срок годности > 7
print(f'Товары со сроком хранения больше {extra_date} дней:')
for i in range(5):
    if products[i].life>extra_date:
        products[i].print_info()