import math
from tkinter import *
def calculate():#функция по высичлению
    x = float(entry.get())
    y = ((math.sqrt(x) * math.sin(x) * (x ** 2 / 2)) - 1.3) / (x ** (1 / 5) + math.exp(3 * x) + abs(math.cos(x)))#формула по вычислению y
    result_label.config(text='Выражение = ' + str(y))#вывод результата
    #создание окна, его титульного нащвания и размеров
window = Tk()
window.title('Формула')
window.geometry('240x150')
#создание метки с x=
x = Label(window, text='x=')
x.place(x=40, y=30)
#создание поля ввода ввода
entry = Entry(window, width=10)
entry.place(x=70, y=30)
#создание кнопки с командой по вычислению
button = Button(window, text='Вычислить', command=calculate)
button.place(x=65, y=60)
#создание метки без ответа
result_label = Label(window, text='Выражение =')
result_label.place(x=10, y=90)
window.mainloop()#вызов окна