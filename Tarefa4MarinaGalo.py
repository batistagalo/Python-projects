""" 
Tarefa da aula 4 BCC

"""
#Atividada 1 - Calcular o volume da esfera dado a variável r (raio)

import numpy as np

    #TESTE 1 - Para raio 0.32 metros, temos:
r= 0.32
v= (4* np.pi)*(r**3)/3 
print ('v =',v, 'metros cúbicos')

    #TESTE 2 - Para raio 1 metro, temos:
r= 1 
v= (4* np.pi)*(r**3)/3
print ('v=',v, 'metros cúbicos')

    #TESTE 3 - Para raio 1.9 metros, temos:
r= 1.9
v= (4* np.pi)*(r**3)/3
print ('v=',v,'metros cúbicos')


#Atividade 2 - Calcular a Temperatura Fahrenheit dado a Temperatura em Celsius (Tc)

    #TESTE 1 - Para -10°C, temos:
Tc = -10
f= (Tc* 1.8) + 32
print ('-10 °C=',f, '°F')
    
    #TESTE 2 - Para 30° C, temos:
Tc= 30
f= (Tc* 1.8) + 32
print ('30 °C=',f, '°F')


    #TESTE 3 - Para 5°C, temos:
Tc= 5
f= (Tc*1.8) + 32
print ('5 °C=',f, '°F')


# Atividade 3 - O tamanho do lado c de um triângulo com lados a,b e ângulo θ entre os lados a e b conhecidos. a, b e θ dado como variáveis. 

import numpy as np

    #TESTE 1
a= 1
b= 2
At= 30
c= np.sqrt( a**2 + b**2 -2* a* b *(np.cos(At)))
print ('c=',c,'cm')

    #TESTE 2
a= 3
b= 1
At= 45
c= np.sqrt( a**2+ b**2 -2* a* b *(np.cos(At)))
print ('c=',c, 'cm')

    #TESTE 3
a= 10
b= 11
At= 15
c= np.sqrt (a**2+ b**2 -2* a* b *(np.cos(At)))
print ('c=',c,'cm')


#Atividade 4 - Mostrar o termo n da série de Fibonacci 

import numpy as np

    #TESTE 1
i= 30 
Fi= np.floor (((((1+ np.sqrt (5))/2)**i) - (((1- np.sqrt(5))/2)**i))/ np.sqrt(5))
print ('Fi=',Fi)

    #TESTE 2
i= 31
Fi= np.floor (((((1+ np.sqrt (5))/2)**i) - (((1- np.sqrt(5))/2)**i))/ np.sqrt(5))
print ('Fi=',Fi)

    #TESTE 3
i= 32
Fi= np.floor (((((1+ np.sqrt (5))/2) **i) - (((1- np.sqrt(5))/2)**i))/ np.sqrt(5))
print ('Fi=',Fi)

