class Vector:#создание класса
    def __init__(self, x, y):#создание двух элементов x и y
        self.x = x
        self.y = y
    def calculate_module(self): #вычисление модулей
        module = (self.x ** 2 + self.y ** 2) ** 0.5
        return module
    def multiply_by_constant(self, k):#умножение на константу
        new_x = k * self.x
        new_y = k * self.y
        return Vector(new_x, new_y)

vector = Vector(4, 7)#создание векторов
module = vector.calculate_module()#вычисление модулей
multiplied_vector = vector.multiply_by_constant(3)#умножение на константу
print('|вектор| =', module)#выводы
print('k*|вектор| =', multiplied_vector.x, multiplied_vector.y)