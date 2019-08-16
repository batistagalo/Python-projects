'''
Tarefa 16- BCC

@author: Marina
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

''' Atividade 1- Faça uma função que receba um vetor t,um valor A, um valor b e 
um valor c e retorne um outro vetor x. A função deve plotar o gráfico de x em 
função de t.'''
print('Atividade 1')
def funçãoX (t, A, b, c):
    '''
    Variáveis da função:
    -----------------------------
    Vetor t: vetor no qual será feita a verificação
    Valor A: valor inteiro
    Valor b: valor 
    Valor c: valor inteiro
    
    Retorna:
    ----------------------------
    - Valores de x no qual são substutuídos os valores de x1, x2 e x3
    Observação: x1, x2 e x3 contem os valores dados para teste
    - Gráfico em função de x 
    '''
    x= A* np.sqrt (1+b*(t**2)) +c
    plt.figure()
    plt.plot(t,x, color= 'dodgerblue')
    plt.xlabel('Valores do vetor t')
    plt.ylabel('Valores do vetor x')
    plt.title('Gráfico de x em função de t')
    plt.grid()
    plt.show()
    return x

x1= funçãoX(np.linspace (0, 10, 1000), 2, 0.5, 0) #Letra a
x2= funçãoX(np.arange (0, 15, 0.2), 10, 0.2, 1) #Letra b
x3= funçãoX(np.linspace (-0.5, 0.5, 500), -3, -1.5, -10) #Letra c
print(  )

''' Atividade 2- Faça uma função que ao ser executada sorteia um número entre 
0 e 1. Se esse número for menor do que 0,5 apareça na tela a mensagem 'Cara'. 
Se esse número for maior do que 0,5 apareça a mensagem 'Coroa'.'''
print('Atividade 2')
def cara_ou_coroa():
    '''
    Parámetro da função:
    -----------------------------
    Salvo na variável "números" os valores aleatórios entre 0 e 1 que serão 
    printados para a confirmação do valor
    
    Retorna:
    ----------------------------
    Se o número for menor que 0.5 retona como "Cara"
    E então o númeor for maior que 0.5 retorna como "Coroa"
    '''
    número= np.random.rand(1)
    print(número)
    if número < 0.5:
        print('Cara')
    else:
        número > 0.5
        print('Coroa')

#Para testar com 5 números diferentes:
for n in range(10):
    cara_ou_coroa()
print(  )
''' Atividade 3- Faça uma função que retorne a moda de uma coluna de um 
DataFrame do Pandas. As entradas devem ser o DataFrame do Pandas e o nome da 
coluna. Além de retornar a moda, a função deve mostrar na tela qual é a moda
encontrada. Para testar a função, compute a moda dos Estádios no campeonato 
brasileiro de futebol de 2018.'''
print('Atividade 3')
#Importar tabela:
Jogos= pd.read_csv('tabelaBrasileirao2018.csv')

def ModaDaColunaQualquer(Data,Coluna):
    '''
    Parâmetros da função:
    -----------------------------
    Para Data deve-se adicionar o nome do DataFrame do Pandas
    Para Coluna deve-se adicionar o nome da Coluna
    
    Observação: não colocar a coluna entre chaves, pois na fómula já consta as
    mesmas
    
    Retorna:
    ----------------------------
    Printado a moda da coluna e o DataFrame do Pandas selecionados
    '''
    Moda= Data[Coluna].value_counts().index[0]
    print('Teste:', Moda)

ModaDaColunaQualquer(Jogos,'Estádio')
ModaDaColunaQualquer(Jogos,'Árbitro')
ModaDaColunaQualquer(Jogos,'Mandante')
print(  )
''' Atividade 4- Dados valores x1, y1, x2, y2, sendo esses valores das 
coordenadas (x1,y1) e (x2,y2) de dois pontos. Fazer uma função que encontre a 
inclinação da reta m e o ponto b em que a reta cruza o eixo y da reta y=mx+b 
que passa pelos dois pontos. Além disso deve ser feito o gráfico da reta encontrada 
com N pontos, além de mostrar os dois pontos dados como entrada, indicados com 
marcadores quadrados. Essa função deve retornar m e b e receber como parâmetros 
x1, y1, x2, y2 e N.'''
print('Atividade 4')
    
def FunçãoInclinação(x1,x2,y1,y2,N):
    '''
    Parâmetros da função:
    -----------------------------
    Velor m: valor que indica a inclinação da reta
    Valor b: valor que o ponto que cruza o eixo y 
    Vetor x: vetor que localiza os valores de N para x1 e x2
    Vetor y: vetor que localiza os valores de N para x1 e x2
    x1 e y1: coordenadas de um ponto do gráfico
    x2 e y2: coordenadas de um outro ponto do gráfico
    
    Retorna:
    ----------------------------
    - Printado os valores da inclinação da reta (m) e o ponto que cruza o eixo y (b)
    - Gráfico dados os valores de a, b e c com os determinados valores de x1,x2,y1,y2 e N
    '''
    m = ((y2- y1)/(x2-x1))
    b = (y1-(m*x1))
    VetorX= np.linspace(x1, x2, N)
    VetorY= np.linspace(y1, y2, N)
    
    print(  )
    print('Inclinação da reta:', m)
    print('Ponto que cruza o eixo y:',b)
    
    plt.figure()
    plt.plot(0, b, color= 'crimson', marker= 's') #Ponto que cruza o eixo y 
    plt.plot(VetorX, VetorY)
    plt.plot(x1,y1, color= 'black', marker= 's') #Ponto entrada
    plt.plot(x2,y2, color= 'black', marker= 's') ##Ponto entrada
    plt.xlabel('Valores de x')
    plt.ylabel('Valores de y')
    plt.title('Gráfico de Inclinação')
    plt.grid()
    plt.show()
   
    return m, b

FunçãoInclinação(-19, 10, 2, -10, 1000) #Letra a
FunçãoInclinação(-2, 20, 8, 43, 2000) #Letra b
FunçãoInclinação(7, 1, 13, 2, 500) #Letra c
