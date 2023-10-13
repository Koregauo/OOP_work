class C:#создание класса
    def __init__(self, a, b=5):#создаём 2 элемента
        self.a=a
        self.b=a

    def c(self):#метод сложения
        return self.a+self.b

    def d(self):#метод разности
        return self.a-self.b

a1=C(5)#считаем сумму
print(f'{a1.a}+{a1.b}={a1.c()}')
a2=C(4,6)#считаем разность
print(f'{a2.a}-{a2.b}={a2.d()}')