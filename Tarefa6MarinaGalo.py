"""
Tarefa 6 - BCC
    

"""
# Atividade 1 - Fazer o gráfico da tensão elétrica medida em um circuito em volts

import numpy as np

    #Variação do tempo (eixo x) e vizualização do vetor utilizado
t= np.arange(0,10.05,0.05)
print('Intervalo do tempo utilizado:', t)

     #Fórmula utilizada
v= ((np.exp(-(0.5*t)))*(np.cos(2*np.pi*0.8*t)))

    #Execução do gráfico (eixo y)
import matplotlib.pyplot as plt
plt.figure()

    #Editar cor da função e tipo da linha
plt.plot (t,v, color= 'darkmagenta', linestyle = '-')

     #Editar nome no eixo da coordenada, abcissa e o nome do gráfico
plt.xlabel('Tempo em segundos')
plt.ylabel('Tensão eletrica em volts')
plt.title('Tensão elétrica medida em um circuito')

     #Para vizualização do gráfico
plt.show ()



#Atividade 2 - Fazer o gráfico da equivalência da temperatura em Fahrenheits 
#dada temperatura em Celsius

import numpy as np

    #Variação da temperatura (eixo x) e vizualização do vetor utilizado
Tc= np.linspace(-20, 100,100) 
print('Pontos de temperatura utiliados:', Tc)

    #Fórmula utilizada
F= (Tc* 1.8) + 32

    #Eecucução do gráfic (eixo y)
import matplotlib.pyplot as plt
plt.figure()

    #Editar cor da função e tipo da linha
plt.plot (Tc,F, color= 'Steelblue', linestyle = '--')

     #Editar nome no eixo da coordenada, abcissa e o nome do gráfico
plt.xlabel('Temperatura em °C')
plt.ylabel('Temperatura em °F')
plt.title('Gráfico de equivalência da temperatura')

     #Para vizualização do gráfico
plt.show ()



#Atividade 3- Fazer o gráfico do número de habitantes entre 1994 e 2020

# Tendo a como ano e P é o número de habitantes

import numpy as np

    #Variação dos anos (eixo x) e vizualização do vetor utilizado
a= np.arange(1994,2021,1)
print('Intervalo dos anos:', a) 

    #Fórmula utilzada (eixo y)
P= (800000*(np.exp((a-1994)/40)))

    #Execução do Gráfico
import matplotlib.pyplot as plt
plt.figure()

    #Editar cor da função e tipo da linha
plt.plot (a,P, color= 'orangered', linestyle = '-', marker= '.')

     #Editar nome no eixo da coordenada, abcissa e o nome do gráfico
plt.xlabel('Anos') 
plt.ylabel('Número de pessoas') 
plt.title('Gráfico do números de habitantes de determinada cidade')

     #Para vizualização do gráfico
plt.show ()
   
    #Arredondamento do número de pessoas 
va= np.floor(P)

    #Mostrar no console a previsão do número de habitantes em 2020
m= np.max(va)
print('No ano de 2020 essa cidade terá', m,'habitantes')