# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:22:30 2019

@author: m.galo
"""

""" Tarefa 5 BCC """

    #Uma bola é lançada ao ar. Suponha que sua altura h, em metros, t segundos após o lançamento
    
import numpy as np

    #Variação do tempo
t= np.arange (0,5,0.1)

    #Fórmula utilizada
x= (-(t**2))+ 4*t

    #Ponto Máximo da parábola
m= np.max(x)
print('Altura máxima',m,'metros')

    #Execução do gráfico
import matplotlib.pyplot as plt
plt.figure()

    #Editar cor da função e tipo da linha
plt.plot (t,x, color= 'orange')

    #Editar nome no eixo da coordenada e abcissa 
plt.ylabel('Tempo em segundos')
plt.xlabel('Altura em metros')
 
    #Editar o nome do gráfico
plt.title('Gráfico do lançamento da bola')

    #Para vizualização do gráfico
plt.show ()