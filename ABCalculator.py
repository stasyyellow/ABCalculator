import tkinter as tk

#Функция закрытия
def do_close():
    root.destroy()
# Главное Окно
root = tk.Tk()
root.geometry("371x411")
root.title("A/B калькулятор")
#Доп. окно
def popup_window():
    window = tk.Toplevel()
    window.geometry("300x350")
    window.title("A/B результат")
    
    #Кнопка закрытия
    btnClosePupup = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=window.destroy)
    btnClosePupup.place(x=551, y=360, width=80,height=25)
# Метка Заголовка
lblTitle = tk.Label(text= "A/B калькулятор", font = ('Helvetica', 15, 'bold'), fg = '#0000cc')
lblTitle.place(x=96, y=39)

# Метка Заголовка Контрольной группы
lblTitle1 = tk.Label(text = 'Контрольная группа', font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle1.place(x=22,y=78)
#Поля контрольной группы
lblVisitors1 = tk.Label(text = "Поситители:", font = ('Helvetica', 10, 'bold'))
lblVisitors1.place(x=22,y=128)

entVisitors1 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entVisitors1.place(x=168,y=128, width=180, height=25)

lblConversion1 = tk.Label(text = "Конверсии:", font = ('Helvetica', 10, 'bold'))
lblConversion1.place(x=22,y=167)

entConversions1 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entConversions1.place(x=168,y=167, width=180, height=25)


#Метка Тестового Заголовка
lblTitle2 = tk.Label(text = 'Тестовая группа', font = ('Helvetica', 12, 'bold'), fg = '#008800')
lblTitle2.place(x=22,y=210)
#Тестовая Группа
lblVisitors2 = tk.Label(text = "Поситители:", font = ('Helvetica', 10, 'bold'))
lblVisitors2.place(x=22,y=249)

entVisitors2 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entVisitors2.place(x=168,y=249, width=180, height=25)

lblConversion2 = tk.Label(text = "Конверсии:", font = ('Helvetica', 10, 'bold'))
lblConversion2.place(x=22,y=288)

entConversions2 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entConversions2.place(x=168,y=291, width=180, height=25)


# Кнопка Рассчитать
btnProcees = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold'), command=popup_window)
btnProcees.place(x=22, y=352,width=90, height=31)

#Кнопка Закрытия
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=257, y=352, width=89, height=31)


root.mainloop()


