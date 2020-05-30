import tkinter as tk

#Главное окно программы
root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry('250x225')
root.title('Индекс веса')
root.iconbitmap(r'ves.ico')

#Виртуальаня картинка для задания размера в пикселях
pixelVirtual = tk.PhotoImage(width=1, height=1)

#Заголовок программы
lable=tk.Label(root, text='Расчёт коэффициента веса', fg="red", bg="black", font="Atial 14")
lable.pack()

#Ввод данных

lable1=tk.Label(root, text='Ваш рост (м)', fg="black", font="Atial 14")
lable1.pack()

EntryA = tk.Entry(root, width=10, font='Arial 16')
EntryA.pack()

lable2=tk.Label(root, text='Ваш вес (кг)', fg="black",font="Atial 14")
lable2.pack()

EntryB = tk.Entry(root, width=10, font='Arial 16')
EntryB.pack()

lable3=tk.Label(root, text='Результат', fg="black", font="Atial 14")
lable3.pack()

EntryC = tk.Entry(root, width=20, font='Arial 16')
EntryC.pack()

def koef(event):
    a = EntryA.get() # берем текст из первого поля
    a = float(a) # преобразуем в число целого типа

    b = EntryB.get() 
    b = int(b)

    result = str(b/(a*a)) # результат переведем в строку для дальнейшего вывода
    EntryC.delete(0, tk.END) # очищаем текстовое поле полностью
    EntryC.insert(0, result) # вставляем результат в начало 

button=tk.Button(root, text='Рассчитать коэффициент веса', fg="black", font="Atial 10")
button.pack()
button.bind("<Button>", koef)
button.place(relx=0.12, rely=0.88)

#Вывод результата

root.mainloop()