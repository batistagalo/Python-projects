"""
Tarefa 19- BCC

@author: Marina
"""
import numpy as np
'''Atividade-1 Faça um script para estimar o valor de π utilizando o método de Monte Carlo.'''
#Números aleatórios (10000) dentro das variáveis:
x=np.random.rand(10000)
y=np.random.rand(10000)
#Coordenadas do centro ao raio (1):
xC= 0.5
yC= 0.5
d= np.zeros(10000)
#Encontrar a distância em relação ao centro de todos os pontos:
for i in range(len(x)):
    d[i]= np.sqrt(((xC-x[i])**2+(yC-y[i])**2))
#Selecionar ponto dentro da Circunferência:
Seleção= d[d<=0.5]
#Calcular e mostrar o valor de pi:
pi= (4*(len(Seleção)/10000))
print ('Valor estimado de pi:', pi)