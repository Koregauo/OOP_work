import tkinter as tk
from random import randint
def roll():#функция броска кубиков
    number = randint(1, 6)#генерация случайного числа от 1 до 6
    label.config(text=str(number))#вывод в метке цифры, которую сгенерировали
    #создание окна, его тутильного названия и размеров
window = tk.Tk()
window.title('Бросок кубика')
window.geometry('300x50')
label = tk.Label(window, text='Брось кубик')#создание метки
label.pack()
button = tk.Button(window, text='Бросить кубик', command=roll)#создание кнопки с командой броска по клику
button.pack()
window.mainloop()#вызов окна
