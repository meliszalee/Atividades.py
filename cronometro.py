from tkinter import *
import tkinter

#cores
cor1 = "#0a0a0a" #preto
cor2 = "#fafcff" #branco
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelho
cor5 = "#dedcdc" #cinza
cor6 = "#3080f0" #azul

janela = Tk()
janela.title("")
janela.geometry('400x250')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

global tempo
global rodar
global contador
global limitador

tempo = '00:00:00'
rodar = False
contador = -5
limitador = 59

def iniciar():
    global tempo
    global contador
    global limitador
    
    if rodar:
        if contador <= -1:
            inicio = 'Começando em ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 15'
            
        else:
            label_tempo['font'] = 'Times 65 bold'
            
            temporaria = str(tempo)
            h, m, s = map(int, temporaria.split(':'))
            
            h = int(h)
            m = int(m)
            s = int(contador)
            
            if (s >= limitador):
                contador = 0
                m += 1
                
            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)
            
            
            temporaria = str(h[-2:]) + ':' + str(m[-2:]) + ':' + str(s[-2:])
            
            label_tempo['text'] = temporaria
            
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador += 1
        
            
def start():
    global rodar
    
    rodar = True
    iniciar()
    
    
def pausar():
    global rodar
    
    rodar = False
    
    
def reiniciar():
    global tempo
    global contador
    
    contador = 0
    
    tempo = '00:00:00'
    label_tempo['text'] = tempo
    



#Labels

label_app = Label(janela, text='Cronômetro', font=('Arial 12'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Times 65 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=35, y=50)

#Botões

botao_iniciar = Button(janela, command=start, text='Iniciar', width=15, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=190)

botao_pausar = Button(janela,  command=pausar, text='Pausar', width=15, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=140, y=190)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=15, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=260, y=190)



janela.mainloop()
