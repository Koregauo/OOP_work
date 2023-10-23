class Student:#создание класса
    def __init__(self,name, group, yspev):#инициализация 3 параметров
        self.name=name
        self.group=group
        self.yspev=yspev

    def ball(self):#функция по поиску ср балла
        return sum(self.yspev)/len(self.yspev)#само вычисление

    def info(self):#функция по получению информации о студенте
        print(f'Студент  {self.name}')#вывод имени
        print(f'Номер группы  {self.group}')#вывод группы
        print(f'Успеваемость  {", ".join(map(str, self.yspev))}')#вывод успеваемости
        print(f'Средний балл  {self.ball()}\n')#вывод ср балла
students=[]#создаём пустой список
for i in range(5):#цикл для каждого студента до 5 включительно
    name=input('Введите фамилию и имя студента ')#ввод Ф И студента
    group=input('Введите номер группы ')#ввод номера группы
    yspev=[int(yspev) for yspev in input('Введите пять оценок через пробел ').split()]#ввод отметок студента
    student=Student(name, group, yspev)#создаём объект класса студент
    students.append(student)#добавление нового объекта класса студент
print('Информация о студентах ')#вывод всей информации о студентах
for student in students:#проходим по каждому студенту в студентах
    student.info()#вызываем ффункцию инфо
sortirovka=sorted(students, key=lambda x: x.ball())#сортировка студентов
print('Список студентов по возрастанию ср балла ')#вывод 'список студентов по возраств=анию ср балла'
for student in sortirovka:#для каждого
    student.info()#выводим информацию