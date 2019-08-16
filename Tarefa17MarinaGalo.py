"""
Tarefa 17- BCC

autor: Marina Galo 
"""
import pandas as pd
import funçoes as fc

''' Atividade 1- Faça uma função que recebe dois vetores ou duas colunas de uma 
DataFrame do Pandas e retorne a correlação r. A função deve estar no mesmo arquivo 
que a função que calcula a regressão. Esse arquivo deve ser importado no script que 
executará o teste abaixo.'''
#Importar tabela:
Jogos= pd.read_csv('tabelaBrasileirao2018.csv')

#Dados da tabela juntamente com a função:
c= fc.corr (Jogos['Público'], Jogos['Renda (R$)'])
print ('A correlação de público e o dado da renda equivale a',c)