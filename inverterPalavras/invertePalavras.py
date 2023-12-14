import tkinter as tk 
from Palavra import Palavra
from tkinter import messagebox as md

janela = tk.Tk()
janela.geometry('320x180')
janela.title('Invertor de palavras')
janela.resizable(False, False)
janela.anchor(anchor = 'center')

palavra = tk.Label(text= 'Palavra:',height= 2, font= ('courier new', 14, 'italic'))
palavra.grid(column= 0, row= 1)

campoPalavra = tk.Entry(width=12, font= ('courier new', 14 ))
campoPalavra.grid(column= 1, row= 1)

def getInput():
    frase = Palavra(campoPalavra.get())
    md.showinfo(title = 'Resultado', message = f' {frase.invertPalavra()}.')

bInverte = tk.Button(janela,text = 'OK', command = getInput, width = 10, font= ('courier new', 14 ))
bInverte.grid(column= 1, row= 3)



janela.mainloop()