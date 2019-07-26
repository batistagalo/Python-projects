"""
Tarefa 11 - BCC

@author: Marina Galo

"""

import numpy as np

#Faça os gráficos com os valores encontrados de y em função de t e dos valores encontrados de v em função de t:

N = 250

v= np.zeros((N))
y= np.zeros((N))
t= np.zeros((N))

v[0]= 10
y[0]= 0
t[0]= 0


for i in range (1, len(v)):
    v[i]= v[i-1] + 0.01*(-9.81)
    y[i]= y[i-1]+0.01*v[i-1]
    t[i]= t[i-1]+0.01

print(v, y, t)

import matplotlib.pyplot as plt

    # Gráfico da distância em função do tempo:
plt.figure()
plt.xlabel('Distância')
plt.ylabel('Tempo')
plt.title('Gráfico da Distância em função do tempo')
plt.plot(t, y, color='red')
plt.show()

    # Gráfico da velociade em função do tempo:
plt.figure()
plt.xlabel('Velociadade')
plt.ylabel('Tempo')
plt.title('Gráfico da Velocidade em fução do tempo')
plt.plot(t,v, color= 'blue')
plt.show()










