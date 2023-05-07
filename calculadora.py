from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calculadora')
root.geometry()




tela = ttk.Frame(root)
tela.grid()

botoes = ttk.Frame(root, borderwidth=100, width=1, height=100, padding=(10, 10, 10, 10))
botoes.grid()
botao1 = ttk.Button(botoes, text="1").grid()
botao2 = ttk.Button(botoes, text='2').grid()
botao3 = ttk.Button(botoes, text='3').grid()
botao4 = ttk.Button(botoes, text='4').grid()
botao5 = ttk.Button(botoes, text='5').grid()
botao6 = ttk.Button(botoes, text='6').grid()
botao7 = ttk.Button(botoes, text='7').grid()
botao8 = ttk.Button(botoes, text='8').grid()
botao9 = ttk.Button(botoes, text='9').grid()



root.mainloop()
