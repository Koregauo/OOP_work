class Trapezia:#создание класса трапеция
    def __init__(self, a, b, c, d):#инициализация сторон
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def perimeter(self):#функция поиска периметра
        return self.a+self.b+self.c+self.d
class Romb:#создание класса ромб
    def __init__(self, a):#инициализация стороны
        self.a=a
    def perimeter(self):#функция поиска периметра
        return 4*self.a
class Rectangle:#создание класса прямоугольник
    def __init__(self, a, b):#инициализация сторон
        self.a=a
        self.b=b
    def perimeter(self):#функция поиска периметра
        return 2*(self.a+self.b)
#создание экземпляров класса
trapezia=Trapezia(3, 6, 3, 8)
romb=Romb(5)
rectangle=Rectangle(4, 7)
#вывод периметра
print('Периметр трапеции ', trapezia.perimeter())
print('Периметр ромба ', romb.perimeter())
print('Периметр прямоугольника ', rectangle.perimeter())