"""
Tarefa 15 - BCC

@author: Marina Galo

"""
import numpy as np

'''Atividade 1- Faça uma função que receba um número a, um número b e um número x. 
Esta função deve retornar True se x estiver entre a e b e False caso contrário. 
Além disso a função deve mostrar uma mensagem dizendo se x está no intervalo 
entre a e b ou não.

Teste para

a) a = -2.5, b = 6.3 e x = 9.1;
b) a = -10, b = 7 e x = 2.2
c) a = 67.2, b = 87.2 e x = 8.1'''


def estaNoIntervalo(a,b,x):
    Intervalo = np.logical_and(a<x, x<b)
    if Intervalo:
        print(x, 'True, está no intervalo')
    else:
        print(x, 'False, não está no intervalo')
        
    return Intervalo 

u= estaNoIntervalo(-2.5, 6.3, 9.1)
y= estaNoIntervalo(-10, 7, 2.2)
z= estaNoIntervalo(67.2, 87.2, 8.1)
