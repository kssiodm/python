import tkinter as tk 
from Pessoa import Pessoa
from datetime import datetime as dt
from tkinter import messagebox as md

# Criar o frame Principal

janela = tk.Tk()
janela.geometry('320x180')
janela.title('Age Calculator')
janela.resizable(False, False)
janela.anchor(anchor = 'center')

#criar lables
nome = tk.Label(text= 'Nome:',height= 2, font= ('courier new', 14, 'italic'))
nome.grid(column= 0, row= 1)

ano = tk.Label(text= 'Ano:', height= 2, font= ('courier new', 14, 'italic'))
ano.grid(column= 0, row= 2)

#criar Campos (fields)

campoNome = tk.Entry(width=12, font= ('courier new', 14 ))
campoNome.grid(column= 1, row= 1)

campoAno = tk.Entry(width=12, font= ('courier new', 14 ))
campoAno.grid(column= 1, row= 2)

#metodo calcular

def getInputs():
    try:
        humano = Pessoa(campoNome.get(), int(campoAno.get()))
        limpar()
        md.showinfo(title = 'Resultado', message = f'Olá {humano.nome}, Você tem {humano.idade()} anos de idade.')
    except ValueError:
        md.showerror(title = 'Erro!', message = 'informe apenas números no campo Ano.')

#metodo limpar
def limpar() -> None:

    lista = [campoNome,campoAno]

    for input in lista:
        input.delete(0, tk.END)

    # campoNome.delete(0, tk.END)
    # campoDia.delete(0, tk.END)
    # campoMes.delete(0, tk.END)
    # campoAno.delete(0, tk.END)   

#Criar botões 

bCalcular = tk.Button(janela,text = 'OK', command = getInputs, width = 10, font= ('courier new', 14 ))
bCalcular.grid(column= 1, row= 5)
bLimpar  = tk.Button(janela,text = 'Limpar',command = limpar, width = 10, font= ('courier new', 14 ))
bLimpar.grid(column= 0, row= 5)



#começar a QUI
janela.mainloop()
