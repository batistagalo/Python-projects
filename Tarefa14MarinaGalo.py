"""
Tarefa 14- BCC

@author: Marina
"""
#Importar:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Atividade 1- Faça o gráfico do torque na direção y (My [Nm]) em função do tempo (Time [s])
#E Mostre na tela a média e o desvio-padrão do torque na direção y

print('Atividade 1')

#Importar tabela:
Balance = pd.read_csv('balance.csv')

#Definindo eixos|:
x = Balance['Time[s]'] #Tempo
y = Balance['My[Nm]'] #Direção de y

# Execução do gráfico:
plt.figure()

#Calcular a média e do torque na direção y:
b= Balance['My[Nm]']
Média= np.mean(b)
print('Média=', Média)
m= Média* np.ones(len((x)))

#Calcular o desvio-padrão na direção y:
Desvio= np.std(b)
print('Desvio-padrão=', Desvio)
Desviopos= ((Média+ Desvio)*np.ones(len((x))))
Desvioneg= ((Média- Desvio)*np.ones(len((x))))

#Editando o eixo da coordenada, abcissa e o nome do gráfico:
plt.xlabel('Tempo em segundos (Time[s])')
plt.ylabel('Direção em nanômetros (My[Nm])')
plt.title('Gráfico do torque')

#Editando linha de balance (amostras):
plt.plot(x, y, color='black', linestyle='-', label= 'Amostras')

#Editando linha de média e de desvio-padrão no gráfico:
plt.plot(x, m, color='red', linestyle='-', label= 'Média')
plt.plot(x, Desviopos, color='dodgerblue', linestyle='--', label= 'Desvio-padrão')
plt.plot(x, Desvioneg, color='dodgerblue', linestyle='--')

#Colocar legenda no gráfico:
plt.legend() 

#Vizualização do gráfico
plt.grid()
plt.show()
print(  )


#Atividade 2- Calcule a mediana da inflação mensal nos meses de março
#Calcule a média da inflação mensal nos meses de março
#Calcule o desvio-padrão da inflação mensal nos meses de março
#Faça o histograma da inflação mensal nos meses de março

print('Atividade 2')

#Importar tabela com dados
Inflação= pd.read_csv('inflacaoMensal.csv')

#Selecionar somente os meses de março da tabela:
Marços= Inflação[np.logical_not(Inflação['Mês'] != 3)]

#Tranformar as inflaçoes dos meses de março:
InflaçãoMarços= Marços['Inflação'].values

#Definindo eixos:
x = Inflação['Ano'] #Anos 
y = Inflação['Inflação'] #Inflações mensais de marços

#Calcular a mediana da inflação mensal nos meses de março:
Ordem= np.sort(InflaçãoMarços) #Ordenar as amostras
Mediana= np.median(Ordem) #Calcular a mediana
print('Mediana =', Mediana)

#Calcular a média da inflação mensal nos meses de março:
Média= np.mean(InflaçãoMarços)
print('Média=', Média)
Média2= Média* np.ones(len((y)))

#Calcule o desvio-padrão da inflação mensal nos meses de março:
Desvio2= np.std(InflaçãoMarços)
print('Desvio-padrão=', Desvio2)
Desviopos2= ((Média2+ Desvio2)*np.ones(len((y))))
Desvioneg2= ((Média2- Desvio2)*np.ones(len((y))))

#Editando o eixo da coordenada, abcissa e o nome do gráfico:
plt.xlabel('Anos')
plt.ylabel('Inflações em %')
plt.title('Gráfico das inflações mensais dos meses de março desde 1944')

#Editando linha de Inflações:
plt.plot(x, y, color='black', linestyle='-', label= 'Inflações')

#Editando linha de média e de desvio-padrão no gráfico:
plt.plot(x, Média2, color='red', linestyle='-', label= 'Média')
plt.plot(x, Desviopos2, color='dodgerblue', linestyle='--', label= 'Desvio-padrão')
plt.plot(x, Desvioneg2, color='dodgerblue', linestyle='--')

#Colocar legenda no gráfico:
plt.legend() 

#Vizualização do gráfico
plt.grid()
plt.show()

#Fazer o histograma da inflação mensal nos meses de março:
plt.figure()
plt.hist (InflaçãoMarços, 4)
plt.title('Histograma da inflação mensal nos meses de março')
plt.grid()
plt.show()
print(  )
#Atividade 3- Calcule a mediana da inflação mensal nos meses de março a partir de 1995
#Calcule a média da inflação mensal nos meses de março a partir de 1995
#Calcule o desvio-padrão da inflação mensal nos meses de março a partir de 1995
#Faça o histograma da inflação mensal nos meses de março a partir de 1995
#Coloque um comentário no seu script comentando a razão da diferença entre a 
#média e a mediana ser alta no segundo item e baixa no terceiro item

print('Atividade 3')

#Importar tabela com dados
Inflação= pd.read_csv('inflacaoMensal.csv')

#Selecionar anos e meses de março a partir de 1995:
Meses= Inflação [np.logical_and(Inflação['Ano'] > 1994, Inflação['Mês'] == 3)]

#Tranformar as inflaçoes dos meses de março a partir de 1995 em um vetor:
Inflação = Meses['Inflação'].values

#Definindo eixos:
x = Meses['Ano'] #Anos de 1995 a 2019
y = Meses['Inflação'] #Inflações mensais de marços

#Calcule a mediana da inflação mensal nos meses de março a partir de 1995:
Ordem2= np.sort(Inflação) #Ordenar as amostrar
Mediana= np.median(Ordem2) #Calcular a mediana
print('Mediana=', Mediana)

#Calcule a média da inflação mensal nos meses de março a partir de 1995:
Média= np.mean(Inflação)
print('Média=', Média)
Média3= Média* np.ones(len((y)))

#Calcule o desvio-padrão da inflação mensal nos meses de março a partir de 1995:
Desvio3= np.std(Inflação)
print('Desvio-padrão=', Desvio3)
Dp= ((Média3+ Desvio3*np.ones(len((y)))))
Dn= ((Média3- Desvio3)*np.ones(len((y))))

#Editando o eixo da coordenada, abcissa e o nome do gráfico:
plt.xlabel('Anos')
plt.ylabel('Inflações em %')
plt.title('Gráfico das inflações mensais de março a partir de 1995')

#Editando linha de Inflações:
plt.plot(x, y, color='black', linestyle='-', label= 'Inflações')

#Editando linha de média e de desvio-padrão no gráfico:
plt.plot(x, Média3, color='red', linestyle='-', label= 'Média')
plt.plot(x, Dp, color='dodgerblue', linestyle='--', label= 'Desvio-padrão')
plt.plot(x, Dn, color='dodgerblue', linestyle='--')

#Colocar legenda no gráfico:
plt.legend() 

#Vizualização do gráfico
plt.grid()
plt.show()

#Faça o histograma da inflação mensal nos meses de março a partir de 1995:
plt.figure ()
plt.title('Histograma das inflações mensais de março a partir de 1995')
plt.hist(y,8)
plt.grid ()
plt.show ()

#Justificativa: Essa diferença se deve ao pico inflacionário altissímo no 
#ano de 1990 apresentado no gráfico inflações mensais dos meses de março desde 
#1944, o que já não ocorreu no gráfico das inflações mensais de março a partir 
#e 1995.Este pico inflacionário foi a razão do aumento das média, mediana e 
#desvio-padrão no segundo item quando relacionado ao terceiro item

print(  )
#Atividade 4- Faça o histograma e a média dos valores gerados para N = 100, N = 1000, N = 10000 e N = 100000

#Criar vetor com os N números gerados:
N = np.array([100,1000,10000,10000])
for i in range(len(N)):
    
    #Para cada N calcular através da variável i os números aleatórios entre 0 e 1:
    Valores = np.random.rand(N[i])
    
    #Para calcular as médias de cada valor N:
    MédiadosValores= np.mean(Valores) 
    
    #Vizualizar as médias geradas:
    print(  )
    print('Média dos N números=', MédiadosValores)
    
    #Gerar os Histogramas de cada valor de N:
    plt.hist (Valores)
    plt.title('Histograma para números aleatórios entre 0 e 1')
    plt.grid ()
    plt.show ()                                         