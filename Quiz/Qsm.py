from tkinter import *
from tkinter import messagebox as mb
import json

class Qsm:

    def __init__(self) -> None:
        self.pergunta__no = 0
        self.mostra_titulo()
        self.mostra_pergunta()
        self.op_escolhida = IntVar()
        self.opcao = self.radio_buttons()
        self.mostrar_opcoes()
        self.buttons()
        self.tam_dados = len(pergunta)
        self.correto = 0 

    def mostrar_resultado(self):

        con_err = self.tam_dados - self.correto
        correto = f'Acertos: {self.correto}'
        erros = f'Erros: {con_err}'

        score = int(self.correto/ self.tam_dados * 100)

        resultado = f'Placar: {score}'
        mb.showinfo('Resultado', f'{resultado}\n{correto}\n{erros}')

    def ver_pergunta(self,pergunta__no) -> bool:
        
        if self.op_escolhida.get() == resposta[pergunta__no]:
            return True

    def btnProx(self):
        if self.ver_pergunta(self.pergunta__no):
            self.correto += 1
            self.pergunta__no += 1 

        if self.pergunta__no == self.tam_dados:
            self.mostrar_resultado()
            janela.destroy()
        else:
            self.mostra_pergunta()
            self.mostrar_opcoes()
    def buttons(self):
        btnProximo = Button(janela,
                            text= 'Proximo', 
                            command= self.btnProx,
                            width= 10, bg= 'black',fg= 'white',
                            font= ('arial, 16, bold'))
        btnProximo.place(x= 350, y= 350)

        btn = Button(janela, text= 'Sair', command= janela.destroy,
                    width= 10, bg= 'black',fg= 'white',
                    font= ('arial, 16, bold'))
        btn.place(x = 700, y = 50)

    def mostrar_opcoes(self):
        val = 0
        
        self.opt_selected.set(0)

        for op in opcoes[self.pergunta__no]:
            self.opcao[val]['text'] = op
            val += 1

    def mostra_pergunta(self):
        pergunta_no = Label(janela, text = questao[self.pergunta__no], width = 60,
        font = ('arial' ,16, 'bold' ), anchor = 'w' )
        pergunta_no.place(x = 70, y = 100)

    def mostra_titulo(self):
        titulo = Label(janela, text= 'Quiz', width = 50, bg = "green",fg = 'white', font = ('arial', 20, 'bold'))
        titulo.place(x = 0, y = 2)

    def radio_buttons(self):
        q_list = []
        
        y_pos = 150
        
        while len(q_list) < 4:
            
            radio_btn = Radiobutton(janela, text = ' ',variable = self.opt_selected,
            value = len(q_list) + 1,font = ('arial', 14))
            
            q_list.append(radio_btn)
            
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
    
        return q_list

janela= Tk()
janela.geometry('800x400')
janela.title('SENAC - Quiz')

with open('./Quiz/dados.json') as f:
    dado = json.load(f)

questao = (dado['perguntas'])
opcoes = (dado['opcoes'])
resposta = (dado['resposta'])


janela.mainloop()