import random
class Student:
    """
    Класс студент
    Атрибуты:
    - name(str): ФИ студента
    - group_number(str): номер группы студента
    - uspev(list): успеваемость студента (список из пяти оценок)
    - sr_ball(float): средний балл студента
    """

    def __init__(self, name, group_number, uspev):#инициализация
        """
        Создает объект класса Student.
        Параметры:
        - name(str): ФИ студента
        - group_number(str): номер группы студента
        - uspev(list): успеваемость студента (список из пяти оценок)
        """
        self.name=name
        self.group_number=group_number
        self.uspev=uspev
        self.sr_ball=sum(self.uspev) / 5

    def print_info(self):#создание функции по выводу информации
        print(f'ФИ  {self.name}\n'
              f'  Номер группы  {self.group_number}\n'
              f'  Успеваемость  {self.uspev}\n'
              f'  Средний балл  {self.sr_ball}\n')

def work_students(num_students):
    """
    Генерирует список студентов.
    Параметры:
    - num_students(int): количество студентов
    Возвращает:
    - students(list): список студентов
    """
    students=[]#
    #перебираем всех студентов, рандомно генерируем их оценки и добавляем в их в пустой список
    for i in range(num_students):
        name=input('Введите фамилию и имя студента ')
        group_number=input('Введите номер группы ')
        uspev=[random.randint(2, 10) for _ in range(5)]
        students.append(Student(name, group_number, uspev))
    return students

