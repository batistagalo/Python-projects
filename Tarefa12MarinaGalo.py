
"""
Tarefa 12 - BCC

Marina Galo
"""
#Atividade 1- Fazer uma aproximação de usando uma fórmula de Leibniz:

#Importar função numpy:
import numpy as np

#Execução dos valores:
for k in range(1,5):
    p = 0
    v = np.array([50,500,1000,10000])#Criar um vetor de diferentes valores
    for i in range (v[k-1] + 1):
        if i % 2 == 0:  #Se o número for par ficará positivo
            p = p + (4 /(2 * i + 1))
        else:   #E se o número for ímpar então ficará negativo
            p = p - (4 /(2 * i + 1))
    print('Valor aproximado de pi:',p)
print(  )    

#Atividade 2- Fazer um gráfico com a taxa de inflação anual em função dos anos, de 1945 a 2018:

#Importar tabela de inflação:
import pandas as pd
Inflação = pd.read_csv('inflacaoMensal.csv')

#Ordenar meses para ano:
Inflação.sort_values(['Ano','Mês'])

#Selecionar somente os anos de 1945 a 2018 na tabela:
Anos = Inflação[np.logical_and(Inflação['Ano'] != 1944 , Inflação['Ano'] < 2019)]

#Selecionando inflações no vetor:
Inf= Inflação['Inflação']

#Selecionando todos os anos entre 1945 e 2018:
a= np.zeros((74))

#Intervalo utilizado de linhas nos respectivos anos (linha 11 a 898):
c=11

#Fórmula utilizada para o cálculo da inflação anual:
for i in range(74):
    a[i]= (((((Inf[c]/100)+1)*((Inf[c+1]/100)+1)*((Inf[c+2]/100)+1)*((Inf[c+3]/100)+1)*((Inf[c+4]/100)+1)*((Inf[c+5]/100)+1)*((Inf[c+6]/100)+1)*((Inf[c+7]/100)+1)*((Inf[c+8]/100)+1)*((Inf[c+9]/100)+1)*((Inf[c+10]/100)+1)*((Inf[c+11]/100)+1))-1)*100)
    c=c+12

#Para importar e executar o gráfico:
import matplotlib.pyplot as plt
plt.figure()

#Para identificar os eixos x e y no Gráfico:
x= np.arange(1945, 2019, 1)
y= (a/100)

#Editar cor da função e tipo da linha:
plt.plot (x, y, color = 'steelblue' , linestyle ='-', marker='.' )

#Editando o eixo da coordenada, abcissa eo nome do gráfico:
plt.xlabel ( 'Ano' )
plt.ylabel ( 'Inflação Anual em %' )
plt.title ( 'Índice de Inflação Anual' )

#Para vixualização do gráfico:
plt.grid()
plt.show()
    
# Atividade 3- Calcular a aproximação de uma onda quadrada seguindo a seguinte
# expressão (a expressão abaixo é calculada utilizando uma teoria matemática 
# conhecida como série de Fourier

#Criar um vetor do Numpy com 10 valores aleatórios entre 0 e 1:

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

t= np.linspace(0, 10, 100000)
N=100000
u=0
for i in range(1 ,N+1, 1):
        u= u +((4/np.pi)*np.sin((2*i-1)*t)/(2*i-1))
        
plt.figure()
plt.plot(t,x, color= 'green')
plt.xlabel('Período')
plt.ylabel('Domínio da função')
plt.grid()
plt.show()

N1 = 10
for i in range(1 ,N1+1, 1):
        u1= u +((4/np.pi)*np.sin((2*i-1)*t)/(2*i-1))
N2=100
for i in range(1 ,N2+1, 1):
        u2= u +((4/np.pi)*np.sin((2*i-1)*t)/(2*i-1))
N3=1000
for i in range(1 ,N3+1, 1):
        u3= u +((4/np.pi)*np.sin((2*i-1)*t)/(2*i-1))
N4 = 10000
for i in range(1 ,N4+1, 1):
        u4= u +((4/np.pi)*np.sin((2*i-1)*t)/(2*i-1))


plt.figure()
plt.plot(t,u1)
plt.plot(t,u2, color= 'green')
plt.plot(t,u3, color='yellow')
plt.plot (t,u4, color='red')

plt.xlabel('Período')
plt.ylabel('Domínio da função')
plt.title('Gráfico da série de Fourier')
plt.grid()
plt.show()
