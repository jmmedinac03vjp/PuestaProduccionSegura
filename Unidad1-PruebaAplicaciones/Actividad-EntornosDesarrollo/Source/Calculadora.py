"""
Projeto - Criar uma calculadora no python
"""
from tkinter import *
from tkinter import ttk

# Cores
cor1 = '#1e1f1e' # Preta
cor2 = '#feffff' # Branca
cor3 = '#38576b' # Azul carregado
cor4 = '#ECEFF1' # Cinza
cor5 = '#FFAB40' # Laranja


janela  = Tk()
janela.title('Calculadora')
janela.geometry("235x310") 
janela.config(bg = cor1)

# Criando frames

Frame_tela = Frame(janela, width= 235, height= 50, bg = cor3)
Frame_tela.grid(row = 0, column= 0)

Frame_quadro = Frame(janela, width= 235, height= 268)
Frame_quadro.grid(row = 1, column= 0)

# Criando a lógica da calculadora


todos_valores = ''
def Entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)   
    # passando o valor para tela
    valor_texto.set(todos_valores)


def Calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    print(resultado)

def LimparTela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
# Criando label]
valor_texto = StringVar()
app_label = Label(Frame_tela, textvariable= valor_texto, width= 16, height=2, padx = 7, relief= FLAT, anchor= "e", justify= RIGHT, font =('Ivy 18'), bg =  cor3, fg = cor2)
app_label.place(x = 0, y = 0 )

# Criando botões

b_1 = Button(Frame_quadro, command= LimparTela ,text = "C", width= 11, height= 2, bg = cor4, font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_1.place(x = 0, y = 0)

b_2 = Button(Frame_quadro, command= lambda: Entrar_valores("%"), text = "%", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_2.place(x = 118, y = 0)

b_3 = Button(Frame_quadro, command= lambda: Entrar_valores("/"),text = "/", width= 5, height= 2, bg = cor5, fg = cor2,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_3.place(x = 177, y = 0)


b_4 = Button(Frame_quadro, command= lambda: Entrar_valores("7"),text = "7", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_4.place(x = 0, y = 52)
b_5 = Button(Frame_quadro, command= lambda: Entrar_valores("8"),text = "8", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_5.place(x = 59, y = 52)
b_6 = Button(Frame_quadro, command= lambda: Entrar_valores("9"),text = "9", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_6.place(x = 118, y = 52)
b_7 = Button(Frame_quadro, command= lambda: Entrar_valores("*"),text = "*", width= 5, height= 2, bg = cor5, fg = cor2,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_7.place(x = 177, y = 52)

b_8 = Button(Frame_quadro, command= lambda: Entrar_valores("4"),text = "4", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_8.place(x = 0, y = 104)
b_9 = Button(Frame_quadro, command= lambda: Entrar_valores("5"),text = "5", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_9.place(x = 59, y = 104)
b_10 = Button(Frame_quadro, command= lambda: Entrar_valores("6"),text = "6", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_10.place(x = 118, y = 104)
b_11 = Button(Frame_quadro, command= lambda: Entrar_valores("-"),text = "-", width= 5, height= 2, bg = cor5, fg = cor2,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_11.place(x = 177, y = 104)

b_12 = Button(Frame_quadro, command= lambda: Entrar_valores("1"),text = "1", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_12.place(x = 0, y = 156)
b_13 = Button(Frame_quadro, command= lambda: Entrar_valores("2"),text = "2", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_13.place(x = 59, y = 156)
b_14 = Button(Frame_quadro, command= lambda: Entrar_valores("3"),text = "3", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_14.place(x = 118, y = 156)
b_15 = Button(Frame_quadro, command= lambda: Entrar_valores("+"),text = "+", width= 5, height= 2, bg = cor5, fg = cor2,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_15.place(x = 177, y = 156)

b_16 = Button(Frame_quadro, command= lambda: Entrar_valores("0"),text = "0", width= 11, height= 2, bg = cor4, font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_16.place(x = 0, y = 208)

b_17 = Button(Frame_quadro, command= lambda: Entrar_valores("."),text = ".", width= 5, height= 2, bg = cor4,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_17.place(x = 118, y = 208)

b_18 = Button(Frame_quadro, command= Calcular, text = "=", width= 5, height= 2, bg = cor5, fg = cor2,font = ('Ivy 13 bold'),relief= RAISED, overrelief= RIDGE)
b_18.place(x = 177, y = 208)

janela.mainloop()