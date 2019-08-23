"""
Created on Sat Aug 17 01:07:20 2019

@author: Marina
"""

import numpy as np
def regressao(x, y):
    '''
    Calcula a inclinação m e o intercepto b da reta de regressão utilizado o
    mÃƒÂ©todo dos máxi­nimos quadrados. 
    
    Parâmetros:
    -------------------------------
    x: vetor
       vetor contendo os valores do vetor x
    
    y: vetor
       vetor contendo os valores do vetor y
       
    Retorna
    -------------------------------
    
    m: float
       inclinação da reta de regressãoo
       
    b: float
       intercepto da reta de regressãoo
    '''
    mediaX = np.mean(x)
    mediaY = np.mean(y)
    desvioX = x - mediaX
    desvioY = y - mediaY
    m = np.sum(desvioX*desvioY)/np.sum(desvioX**2)
    b = mediaY - m*mediaX
    
    return m, b

def corr(x, y):
    '''
    Calcula o coeficiente de correlação
    
    Parâmetros:
    -------------------------------
    x: vetor
       vetor contendo os valores do vetor x
    
    y: vetor
       vetor contendo os valores do vetor y
       
    Retorna
    -------------------------------
    
    r: float
        coeficiente de correlação
    '''
    mediaX = np.mean(x)
    mediaY = np.mean(y)
    desvioX = x - mediaX
    desvioY = y - mediaY
    varX = np.sqrt(np.sum(desvioX**2))
    varY = np.sqrt(np.sum(desvioY**2))
    r = np.sum(desvioX*desvioY)/(varX*varY)
    
    return r