''' Tarefa 9 - BCC
  
    Marina Galo '''
    

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


    # Atividade: Fazer um gráfico da taxa de analfabetismo em São Paulo em função dos anos
    
plt.figure()

    #Para abir a coluna de São Paulo:
analfabetismo= pd.read_csv('analfabetismo.csv')

print('Dados utilizados:')
print(  )

    #Para o eixo y no gráfico:
print('Dados utilizados:')
a= analfabetismo['São Paulo']
print('Taxa em porcentagem:',a)

print(  )

    #Para o eixo x no gráfico:
b= analfabetismo['Ano']
print('Anos:', b)

    #Editar cor da função e tipo da linha:
plt.plot (b,a, color= 'indigo', linestyle = ':', marker = '.')

     #Editar nome no eixo da coordenada, abcissa e o nome do gráfico:
plt.xlabel('Anos')
plt.ylabel('Taxa em porcentagem')
plt.title('Analfabetismo no Estado de São Paulo')

     #Para vizualização do gráfico:
plt.grid()
plt.show ()
