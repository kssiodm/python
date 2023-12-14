import tkinter as tk

janela = tk.Tk()
janela.geometry('450x300')
janela.title('tk')
janela.resizable(False, False)

def limpar() -> None:
    campoNumero.delete(0, tk.END)
    lblResultado['text'] = 'calculando...'

def fatorial():
    numero = int(campoNumero.get())

    resultado=1
    for n in range(1,numero +1):
        resultado *= n

    lblResultado['text'] = f'o fatorial de {campoNumero}! = {resultado} '

lblNumero = tk.Label(janela, text = 'informe o numero fatorial:', font= ('courier new', 14, 'italic'))
lblNumero.place(x = 20, y = 20)

campoNumero = tk.Entry(janela,  font= ('courier new', 14))
campoNumero.place(x = 200, y = 20)

lblResultado = tk.Label(janela, text = 'calculando...',   font= ('courier new', 11) )
lblResultado.place(x = 20, y = 70)

btnCalcular = tk.Button(janela, text= 'calcular', command = fatorial, font= ('courier new', 14))
btnCalcular.place(x = 190, y = 100)

btnLimpar = tk.Button(janela, text= 'Limpar', command = limpar, font= ('courier new', 14))
btnLimpar.place(x= 300 , y = 100)

janela.mainloop()