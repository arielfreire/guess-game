from tkinter import *
from tkinter import messagebox

import random

def reset():
    reset = messagebox.askyesno("Guessgame","Tem certeza que deseja reiniciar o jogo?")
    if reset == True:
            inicializaVariaveisGlobais()
            return

def processaTecla(evento):
    testaPalpite()

def setStatus():
    global plpt, alvo
    if   abs(plpt-alvo) <= 3: status = ['FV',abs(plpt-alvo)]
    elif abs(plpt-alvo) <= 5: status = ['MQ',abs(plpt-alvo)]
    elif abs(plpt-alvo) <= 8: status = ['QT',abs(plpt-alvo)]
    elif abs(plpt-alvo) <= 13: status = ['MR',abs(plpt-alvo)]
    elif abs(plpt-alvo) <= 21: status = ['FR',abs(plpt-alvo)]
    elif abs(plpt-alvo) <= 34: status = ['MF',abs(plpt-alvo)]
    else                 : status = ['CG',abs(plpt-alvo)]

    return status

def fornecePista(st1, st2):
    global dica
    if   st1[0] == 'FV': #Fervendo
        if st2[0] == 'FV':
            if st2[1] < st1[1]:
                dica = 'Ainda esta FERVENDO! Mas esquentou.'
            else: dica = 'Ainda esta FERVENDO! Mas esfriou.'
        elif st2[0] == 'MQ': dica = 'Esfriou, mas ainda continua muito quente.'
        elif st2[0] == 'QT': dica = 'Oops, deu uma esfriada, mas ainda está quente.'
        elif st2[0] == 'MN': dica = 'Oops, deu uma esfriada, agora esta morno.'
        elif st2[0] == 'FR': dica = 'Oops, agora ficou frio.'
        elif st2[0] == 'MF': dica = 'OOps, agora ficou muito frio.'
        elif st2[0] == 'CG': dica = 'Oops, deu uma mega esfriada! Agora esta CONGELANDO!'
        else            : dica = 'Esta FERVENDO!'
    elif   st1[0] == 'MQ':#Muito quente
        if st2[0] == 'FV':dica = 'Esquentou! Agora esta FERVENDO!'
        elif st2[0] == 'MQ':
            if st2[1] < st1[1]:
                dica = 'Ainda esta muito quente. Mas esquentou.'
            else: dica = 'Ainda esta muito quente. Mas esfriou.'
        elif st2[0] == 'QT': dica = 'Oops, deu uma esfriada, mas ainda está quente.'
        elif st2[0] == 'MN': dica = 'Oops, deu uma esfriada, agora esta morno.'
        elif st2[0] == 'FR': dica = 'Oops, agora ficou frio.'
        elif st2[0] == 'MF': dica = 'OOps, agora ficou muito frio.'
        elif st2[0] == 'CG': dica = 'Oops, deu uma mega esfriada! Agora esta CONGELANDO!'
        else            : dica = 'Está muito quente.'
    elif st1[0] == 'QT': #Quente
        if st2[0] == 'FV': dica = 'Esquentou! Agora esta FERVENDO!'
        elif st2[0] == 'MQ': dica = 'Opa! Deu uma esquentada e agora ficou muito quente.'
        elif st2[0] == 'QT':
            if st2[1] < st1[1]:
                dica = 'Ainda esta quente. Mas esquentou.'
            else: dica = 'Ainda esta quente. Mas esfriou.'
        elif st2[0] == 'MN': dica = 'Oops, deu uma esfriada, agora esta morno.'
        elif st2[0] == 'FR': dica = 'Oops, deu uma boa esfriada e agora ficou frio.'
        elif st2[0] == 'MF': dica = 'Oops, deu uma super esfriada e agora ficou muito frio.'
        elif st2[0] == 'CG': dica = 'Oops, deu uma mega esfriada! Agora esta CONGELANDO!'
        else            : dica = 'Está quente.'
    elif st1[0] == 'MN': #Morno
        if st2[0] == 'FV': dica = 'Esquentou! Agora esta FERVENDO!'
        elif st2[0] == 'MQ': dica = 'Opa! Deu uma esquentada e agora ficou muito quente.'
        elif st2[0] == 'QT': dica = 'Opa! Deu uma esquentada e agora ficou quente.'
        elif st2[0] == 'MN':
            if st2[1] < st1[1]:
                dica = 'Ainda esta morno. Mas esquentou.'
            else: dica = 'Ainda esta morno. Mas esfriou.'
        elif st2[0] == 'FR': dica = 'Oops, deu uma esfriada e agora ficou frio.'
        elif st2[0] == 'MF': dica = 'Oops, deu uma boa esfriada e agora ficou muito frio.'
        elif st2[0] == 'CG': dica = 'Oops, deu uma mega esfriada! Agora esta CONGELANDO!'
        else            : dica = 'Está morno.'
    elif st1[0] == 'FR': #Frio
        if st2[0] == 'FV': dica = 'Esquentou! Agora esta FERVENDO!'
        elif st2[0] == 'MQ': dica = 'Oops, deu uma baita esquentada e agora ficou muito quente.'
        elif st2[0] == 'QT': dica = 'Oops, deu uma esquentada e agora ficou quente.'
        elif st2[0] == 'MN': dica = 'Esquentou, agora esta morno.'
        elif st2[0] == 'FR':
            if st2[1] < st1[1]:
                dica = 'Ainda esta frio. Mas esquentou.'
            else: dica = 'Ainda esta frio. Mas esfriou.'
        elif st2[0] == 'MF': dica = 'Oops, deu uma esfriada e agora ficou muito frio.'
        elif st2[0] == 'CG': dica = 'Oops, deu uma mega esfriada! Agora esta CONGELANDO!.'
        else            : dica = 'Está frio.'
    elif st1[0] == 'MF': #Muito Frio
        if st2[0] == 'FV': dica = 'Esquentou! Agora esta FERVENDO!'
        elif st2[0] == 'MQ': dica = 'Oops, deu uma baita esquentada e agora ficou muito quente.'
        elif st2[0] == 'QT': dica = 'Oops, deu uma esquentada e agora ficou quente.'
        elif st2[0] == 'MN': dica = 'Esquentou, agora esta morno.'
        elif st2[0] == 'FR': dica = 'Oops, deu uma esquentada, mas está frio.'
        elif st2[0] == 'MF':
            if st2[1] < st1[1]:
                dica = 'Ainda esta muito frio. Mas esquentou.'
            else: dica = 'Ainda esta muito frio. Mas esfriou.'
        elif st2[0] == 'CG': dica = 'Oops, deu uma esfriada! Agora esta CONGELANDO!.'
        else            : dica = 'Está muito frio.'
    elif st1[0] == 'CG': #Congelando
        if st2[0] == 'FV': dica = 'Esquentou! Agora esta FERVENDO!'
        elif st2[0] == 'MQ': dica = 'Oops, deu uma mega esquentada e agora ficou muito quente.'
        elif st2[0] == 'QT': dica = 'Oops, deu uma super esquentada e agora ficou quente.'
        elif st2[0] == 'MN': dica = 'Esquentou, agora esta morno.'
        elif st2[0] == 'FR': dica = 'Oops, deu uma esquentada, mas está frio.'
        elif st2[0] == 'MF': dica = 'Oops, deu uma esquentada, mas está muito frio.'
        elif st2[0] == 'CG':
            if st2[1] < st1[1]:
                dica = 'Ainda esta CONGELANDO. Mas esquentou.'
            else: dica = 'Ainda esta CONGELANDO. Mas esfriou.'
        else:
            dica = 'Está CONGELANDO.'

    return dica

def inicializaVariaveisGlobais():
    global pista, alvo, numerosJogados, memória
    global jogadas, chances, palpite, plpt, memlbl

    alvo = random.randint(1,100)  # inicializa número alvo
    numerosJogados = []           # inicializa lista dos números jogados
    jogadas = 10                  # inicializa contador de jogadas
    chances.set(jogadas)
    palpite.set("")
    memlbl.set("")
    memória.set("")
    pista.set("")
    photo.config(file = "./res/restart.png")
    dica = ""
    print(alvo)
    
def palpiteVálido(palpite):

    # verifica se o valor do palpite é um número inteiro
    # se não fôr, atribui um inteiro inválido

    try:
        palpite = int(palpite)
    except:
        palpite = 0

    # checa se o palpite é válido
    # se for, retorna o valor do palpite
    # se não for, emite mensagem de erro e retorn False
    
    if (palpite >= 1) and (palpite <= 100):
        return palpite
    else:
        return False

def testaPalpite():
    global alvo, palpite, jogadas, chances, root, plpt
    global numerosJogados, status1, status2, pista, pst
    global memória, memlbl
    
    # obtém palpite do usuário
    strPalpite = palpite.get()

    # recupera estado do palpite
    plpt = palpiteVálido(strPalpite)
    
    # verifica se o valor do palpite é válido
    # caso afirmativo, segue em frente
    if plpt:
        pass
    else:                 # se palpite for inválido:
        messagebox.showerror("Erro", "Número inválido!\nTente de novo.")
        palpite.set("")   #    limpa o campo de palpite
        return            #    retorna ao tabuleiro

    # verifica se o palpite já foi tentado antes    
    # se tiver sido, emite mensagem de aviso
    # limpa o campo de palpite e retorna ao tabuleiro
    if plpt in numerosJogados:   
        messagebox.showwarning("Aviso", "Você já tentou este número!\nTente de novo.")
        palpite.set("")
        return

    # verifica se o jogador acertou o alvo
    # se acertou, emite mensagem de parabéns e pergunta se ele quer jogar de novo
    # se ele quiser, reinicializa as variáveis do jogo e retorna ao tabuleiro
    # caso contrário, encerra o jogo
    if plpt == alvo:
        photo.config(file = "./res/right.png")
        resp = messagebox.askyesno("Guessgame","Parabéns!!\nVocê acertou o alvo.\nQuer jogar de novo?")
        if resp == True:
            inicializaVariaveisGlobais()
            return
        else:
            root.destroy()
        
    # no caso do palpite ser válido mas diferente do alvo:
    # determina status do palpite
    photo.config(file = "./res/error.png")
    if len(numerosJogados) == 0:    # se for o primeiro palpite:
        status1 = setStatus()       #    determina status do primeiro palpite
        status2 = ['',0]                #    seta status2 com nulo
    elif len(numerosJogados) == 1:  # se for o segundo palpite:
        status2 = setStatus()       #    determina status do segundo palpite
    else:                           # do terceiro palpite em diante:
        status1 = status2           #    seta status do palpite anterior
        status2 = setStatus()       #    determina status do palpite corrente

    # determina pista para o usuário
    dica = fornecePista(status1, status2)
    # fornece pista ao jogador
    pista.set(dica)

    #
    # contabiliza palpite
    #
    #    inclui palpite na lista de números jogados
    numerosJogados.append(plpt)
    #    atualiza a memória de números jogados
    mem = memória.get()
    if mem == "": mem = str(plpt)
    else        : mem += " - " + str(plpt)
    memória.set(mem)

    # reduz número de chances e atualiza o tabuleiro
    jogadas -= 1
    chances.set(jogadas)
    # limpa o campo de palpite
    palpite.set("")
    if jogadas == 0 and plpt !=alvo:
        resp2 = messagebox.askyesno("Perdeu!","Infelizmente após 10 tentativas você não acertou o numero "+ str(alvo) +".\n Deseja jogar novamente?")
        if resp2 == True:
            inicializaVariaveisGlobais()
            return
        else:
            root.destroy()
        
    # retorna ao tabuleiro
    return

def limpaPalpite():
    global palpite
    # limpa o campo de palpite
    palpite.set("")

#
#------------- Criação da janela raiz
#
root = Tk()
root.configure(bg="#6495ED")
root.title("Guessgame")
#
#------------- Definição dos frames de posicionamento
#
f0 = Frame(root, width=800, height=400, padx=20, bg="#6495ED")
f0.pack(side=TOP)

fl = Frame(root, width=800, pady=4, bg="#6495ED")
fl.pack()

f2 = Frame(root, width=800, pady=8, bg="#6495ED")
f2.pack()

f3 = Frame(root, width=800, pady=8, bg="#6495ED")
f3.pack()
#
#------------- Define variáveis Tk
#
chances = StringVar()    # variável Tk que indica o número de chances restantes
palpite = StringVar()    # variável Tk que indica o palpite corrente do usuário
pista = StringVar()      # variável Tk que indica a pista fornecida ao usuário
memória = StringVar()    # variável Tk que indica os números já jogados
memlbl = StringVar()     # variável Tk que indica o rótulo do campo de memória
#
#------------- Definição e posicionamento dos widgets
#
photo_guess = PhotoImage(file = "./res/guess.png")
Label(f0,image = photo_guess , bg="#6495ED", pady=16).grid(row=0)
Label(f0, font=("Franklin Gothic Heavy", "12"), justify="center", \
      bd=1, bg="#4682B4", fg="white", relief=RIDGE, padx= 20, pady=20, \
      text="O objetivo desse jogo é descobrir o valor que estou pensando:\n\n \
 Trata-se de um valor entre 1 e 100 e você terá 10 chances para acertá-lo.\n \
 A cada tentativa, eu lhe darei uma pista sobre a proximidade do seu palpite\n \
      em relação ao alvo que eu estabeleci.\n \
 A todo momento, você poderá encerrar ou reiniciar o jogo sem ter de esperar\n \
      o final de uma jogada, isto é, sem ter de esperar por sua décima chance.") \
   .grid(row=1)
photo = PhotoImage(file = "./res/restart.png")
Label(f0, image = photo,bg="#6495ED").grid(row=2)
#-------------
Label(fl, text ="Você possui ", font=("Arial Narrow", "12"), bg="#4682B4", fg="white").grid(row=0, column=0, pady=12, sticky=E)
Label(fl, textvariable=chances, font=("Arial Narrow", "12", "bold"), bg="#4682B4", fg="#B0C4DE").grid(row=0, column=1, sticky=W)
Label(fl, text=" tentativas.", font=("Arial Narrow", "12"), bg="#4682B4", fg="white").grid(row=0, column=2, sticky=W)

#-------------
Label(f2, text="Seu palpite: ", font=("Arial Narrow", "12"), bg="#6495ED", fg="white").grid(row=0, column=0, sticky=E)
plpt = Entry(f2, textvariable=palpite, font=("Arial Narrow", "12", "bold"), width=5, bg="#008B8B", fg="white", bd=3, justify=CENTER)
plpt.grid(row=0, column=1, sticky=E)
plpt.bind("<Return>", processaTecla)
#-------------
btnTestar = Button(f2,text="Testar",command=testaPalpite, relief=RAISED, bg="#4682B4", fg="white", \
                   font=("Arial Narrow", "10"), width=6).grid(row=1, column=0, padx=4, pady=12, sticky=W)
btnLimpar = Button(f2,text="Limpar",command=limpaPalpite,  relief=RAISED, bg="#4682B4", fg="white", \
                   font=("Arial Narrow", "10"), width=6).grid(row=1, column=1, sticky=E)
#btnTestar.bind("<Return>", processaTecla)
#btnLimpar.bind("<Return>", processaTecla)
#-------------
Label(f3, textvariable=memlbl,  font=("Arial Narrow", "12", "bold"), bg="#6495ED", fg="#44546A").grid(row=0, column=0, pady=10, sticky=E)
Label(f3, textvariable=memória, font=("Arial Narrow", "12", "bold"), bg="#6495ED", fg="white").grid(row=0, column=1, sticky=W)

Label(f3, text="Dica: ", font=("Arial Narrow", "12", "bold"), bg="#6495ED", fg="white") \
      .grid(row=1, column=0, pady=5, sticky=E)
pst = Label(f3, textvariable=pista, font=("Arial Narrow", "12", "bold"), bg="#6495ED", fg="black", width=50, relief=RIDGE, bd=4) \
      .grid(row=1, column=1, sticky=W)
btnLimpar = Button(f3,text="Reiniciar",command=reset,  relief=RAISED, bg="#4682B4", fg="white", \
                   font=("Arial Narrow", "10"), width=6).grid(row=1, column=2)

#
#------------- Inicia Jogo
#
plpt.focus()
inicializaVariaveisGlobais()

root.mainloop()

