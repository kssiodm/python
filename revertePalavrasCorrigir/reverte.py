import tkinter as tk

frame = tk.Tk()
frame.geometry('470x200')
frame.title('tk')
frame.resizable(False, False)

def limpar() -> None:
    campoFrase.delete(0, tk.END)
    lblResultado['text'] = 'Resultado...'

def reverter():
    frase = campoFrase.get()
    frase_reverse = ' '

    for i in frase:
        frase_reverse = i + frase_reverse

    lblResultado['text'] = frase_reverse


lblFrase = tk.Label(frame, text = 'informe a frase:', font= ('courier new', 14, 'italic'))
lblFrase.place(x = 20, y = 20)

campoFrase = tk.Entry(frame,  font= ('courier new', 14))
campoFrase.place(x = 190, y = 20)

lblResultado = tk.Label(frame, text = 'Resultado...',  font= ('courier new', 11) )
lblResultado.place(x = 20, y = 70)

btnReverter = tk.Button(frame, text= 'Iniciar', command= reverter, font= ('courier new', 14))
btnReverter.place(x = 190, y = 100)

btnLimpar = tk.Button(frame, text= 'Limpar', command = limpar, font= ('courier new', 14))
btnLimpar.place(x= 290 , y = 100)

frame.mainloop()