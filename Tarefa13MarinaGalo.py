# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:38:38 2019

@author: m.galo
"""
#Atividade 1- Escolha um time e faça o histograma da distribuição do público nos jogos em que este time foi o mandante.
#Calcule qual foi o público médio nos jogos em que o time escolhido foi o mandante

#Importando:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Calculando média do público dos jogos do Palmeiras:
Jogos= pd.read_csv('tabelaBrasileirao2018.csv')
Média= Jogos[Jogos['Mandante']== 'Palmeiras']['Público'].mean()
Média2= np.floor(Média)
print('Média de pessoas nos jogos do Palmeiras:', Média2)

#Mostrando o histograma:
plt.figure()
plt.hist(Jogos[Jogos['Mandante']== 'Palmeiras']['Público'],8)
plt.grid()
plt.show()