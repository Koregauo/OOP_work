class Student:
    def __init__(self,name, group, yspev):
        self.name=name
        self.group=group
        self.yspev=yspev

    def ball(self):
        return sum(self.yspev)/len(self.yspev)

    def info(self):
        print(f'Студент  {self.name}')
        print(f'Номер группы  {self.group}')
        print(f'Успеваемость  {", ".join(map(str, self.yspev))}')
        print(f'Средний балл  {self.ball()}\n')
students=[]
for i in range(5):
    name=input('Введите фамилию и имя студента ')
    group=input('Введите номер группы ')
    yspev=[int(yspev) for yspev in input('Введите пять оценок через пробел ').split()]
    student=Student(name, group, yspev)
    students.append(student)
print('Информация о студентах ')
for student in students:
    student.info()
sortirovka=sorted(students, key=lambda x: x.ball())
print('Список студентов по возрастанию ср балла ')
for student in sortirovka:
    student.info()