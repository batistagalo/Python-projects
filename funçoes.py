# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:47:32 2019

@author: m.galo
"""
import numpy as np

def corr(x,y,):
    mediaX= np.mean(x)
    mediaY= np.mean(y)
    desvioX= (x-mediaX)
    desvioY= (y-mediaY)
    somaXY= np.sum(desvioX*desvioY)
    raizsomaX2= np.sqrt(np.sum(desvioX**2))
    raizsomaY2=np.sqrt(np.sum(desvioY**2))
    
    r= somaXY/(raizsomaX2*raizsomaY2)
    
    
    return r