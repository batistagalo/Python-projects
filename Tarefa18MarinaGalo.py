'''
Tarefa 18- BCC

@author: Marina
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Funções as fc

'''Atividade 1- Faça o gráfico de dispersão do tamanho do pé (FootLen) em 
função da altura da pessoa (Height). Calcule (e mostre na tela) a correlação e 
plote a reta de regressão entre esses dados.'''
#Importar tabela:
Tabela = pd.read_csv('BDSinfo.csv', delimiter='\t')

#Calculando váriaveis utilizando a função de regressão:
x1,y1 = fc.regressao(Tabela['Height'],Tabela['FootLen'])
print('Exercício 1')

#Calcular a Correlação:
c1= fc.corr(Tabela['Height'],Tabela['FootLen'])
print('Valor da correlação:',c1)

#Vizualizar o gráfico:
plt.figure()
plt.plot(Tabela['Height'], Tabela['FootLen'], marker='o', color='red', linestyle='')
plt.plot(Tabela['Height'], x1*Tabela['Height']+y1, color='dodgerblue', linestyle='-')
plt.xlabel('Altura da pessoa (cm)')
plt.ylabel('Tamanho do pé (cm)')
plt.title('Gráfico de Dispersão com reta de Regressão: Altura x Tamanho do pé')
plt.grid()
plt.show()
print(  )
'''Atividade 2- Faça o gráfico de dispersão entre o crescimento do PIB e a 
inflação anual de 1961 a 2018. Calcule e mostre na tela a correlação entre as 
duas grandezas.'''
#Importar tabelas:
PIBAnual= pd.read_csv('pibAnual.csv')
InflaçãoAnual= pd.read_csv('inflaAnual.csv')

#Selecionar PIB na tabela:
PIBAnualReal= PIBAnual['Variação anual do PIB real (%)']

#Selecionar Inflação anual dos anos de 1961 a 2018 na tabela:
Anos= InflaçãoAnual[np.logical_and(InflaçãoAnual['Ano']>1960, InflaçãoAnual['Ano'] <= 2018)]
InflaçãoAnualReal= Anos['Inflação']
print('Exercício 2')
#Calcular a Correlação:
c2= fc.corr(PIBAnualReal,InflaçãoAnualReal)
print('Valor da correlação:',c2)

#Vizualizar o gráfico:
plt.figure()
plt.plot(PIBAnualReal,InflaçãoAnualReal, marker='o', color='red', linestyle='')
plt.xlabel('PIB Anual')
plt.ylabel('Inflação Anual')
plt.title('Gráfico de Dispersão entre o crescimento do PIB e a inflação anual de 1961 a 2018')
plt.grid()
plt.show()
print(  )
'''Atividade 3- Faça o gráfico de dispersão do número de medicamentos que a 
pessoa toma (Nmedication) em função da idade da pessoa (Age). Calcule (e mostre
na tela) a correlação e plote a reta de regressão entre esses dados. Importe 
da base com informacoes pessoais.'''
#Importar tabela:
Tabela= pd.read_csv('BDSinfo.csv', delimiter='\t')

#Calculando váriaveis utilizando a função de regressão:
x2,y2 = fc.regressao(Tabela['Age'],Tabela['Nmedication'])
print('Exercício 3')
#Calcular a Correlação:
c3= fc.corr(Tabela['Age'],Tabela['Nmedication'])
print('Valor da correlação:',c3)

#Vizualizar o gráfico:
plt.figure()
plt.plot(Tabela['Age'],Tabela['Nmedication'], marker='o', color='red', linestyle='')
plt.plot(Tabela['Age'], x2*Tabela['Age']+y2, color='dodgerblue', linestyle='-')
plt.xlabel('Idade da pessoa em anos')
plt.ylabel('Número de medicamentos que a pessoa toma')
plt.title('Gráfico de Dispersão com reta de Regressão: Idade x N° de medicamentos')
plt.grid()
plt.show()