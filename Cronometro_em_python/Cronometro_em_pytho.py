from tkinter import *
import tkinter

#cores groblais------------------------------
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

#Janela Global-----------------------------------
janela = Tk()
janela.title("Cronômetro")
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=False, height=False)


#passo 3 definindo vaiaveis globais

global tempo
global rodar
global contador
global limitador


limitador = 59


#passo 2 do projeto criar as funções do projeto
limitador = 59
tempo = "00:00:00"
rodar = False
contador = -5

# funcao iniciar
def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        # antes do cronometro começar
        if contador <=-1:
            inicio = 'Começando em ' +str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10 '

        # Rodando o cronômetro
        else:  
            label_tempo['font'] = 'Times 50 bold'

            temporario = str(tempo) 
            h,m,s = map(int,temporario.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s>=limitador):
                contador = 0
                m+=1
            
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            temporario = str(h[-2:])+":" + str(m[-2:])+ ":" + str(s[-2:])
            label_tempo['text'] = temporario
            tempo = temporario


        label_tempo.after(1000,iniciar)
        contador +=1

#funcao para dar inicio 
def start():
    global rodar
    rodar = True
    iniciar()

#funcao para pausar
def pausar():
    global rodar
    rodar = False


def reiniciar():
    global contador
    global tempo

    #reiniciando o tempo e o contador
    contador = 0
    #reiniciando o tempo 
    tempo = "00:00:00"
    label_tempo['text'] = tempo



#passo 1 do projeto criar a janelas e os labels 
#Label 01 - mostra os números do aplicativo ----
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)
#label 02 - Tempo mostra o tempo do aplicativo --
label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=30)

#label 03 botões - botão 01 iniciar do aplicativo --------
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

#label 04 botões  - botão 02 pausar do aplicativo --------
botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

#label 05 botões  - botão  03 reiniciar do aplicativo --------
botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130)

iniciar()


janela.mainloop()
