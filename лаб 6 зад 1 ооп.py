from module import Student, work_students
def by_gpa_key(student):
    """
    Функция-ключ для сортировки студентов по среднему баллу.
    Параметры:
    - student(Student): объект класса Student
    Возвращает:
    - sr_ball(float): средний балл студента
    """
    return student.sr_ball
#перебор студентов и их сортировка
if __name__=='__main__':
    num_students=10
    students=work_students(num_students)
    students_sort=sorted(students, key=by_gpa_key)
    for student in students_sort:
        student.print_info()

