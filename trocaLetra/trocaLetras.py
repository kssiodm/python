import tkinter as tk

janela = tk.Tk()
janela.geometry('300x300')
janela.title('Trocar caracter.')
janela.resizable(False, False)

def getReplce():
    str1 = 'B'
    str2 = '#'

    cp1 = 'Frase de entrada'
    cp2 = cp1.replace(str1, str2)

campo1 = tk.Entry(janela)
campo1.place(x=30 , y=30)
campo2 = tk.Entry(janela)
campo2.place(x=30 , y=90)

janela.mainloop()