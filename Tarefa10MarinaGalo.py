"""
Tarefa 10 - BCC

Marina Galo
"""

#Atividade 1- Calculae e mostrar a porcentagem de jogos que o time da casa ganhou o jogo 
#E calcular e mostrar a porcentagem de jogos que o time da casa não perdeu o jogo

import pandas as pd
import numpy as np

    #Importar tabela e dados:
Jogos = pd.read_csv('tabelaBrasileirao2018.csv')

     #Parámetro utilizado:
Jogos['Derrotas'] = Jogos ['Placar do Mandante'] < Jogos ['Placar do Visitante']
Jogos['Vitórias'] = Jogos ['Placar do Mandante'] > Jogos ['Placar do Visitante']
Jogos['Empates'] = Jogos ['Placar do Mandante'] == Jogos ['Placar do Visitante']

    #Mostrar a porcentagem de vitórias:
    #Sendo 202 a quantodade de jogos ganhos e 380 o total de jogos, temos a porcentagem:
    
c = Jogos['Vitórias'].value_counts()
v = np.floor(((202/380)*100))
print(v, '% somente de vitórias do Time Mandante')

    #Calculae e mostrar a porcentagem de jogos que o time da casa ganhou ou empatou:
    #Sendo 202 o número de vitórias, 110 o número de empates e 380 o total de jogos, temos a porcentagem:

i = Jogos['Vitórias'].value_counts()
e = Jogos['Empates'].value_counts()

t = np.floor(((312/380)*100))
print (t,'% de vitórias e empates do Time Mandante')



#Atividade 2- Faça um gráfico da taxa de inflação mensal em função do tempo
#Mostre em que mês e ano e qual foi a maior taxa de inflação mensal medida de fevereiro de 1944 a junho de 2019)

    #Importar tabela e dados:
import pandas as pd
inflação = pd.read_csv('inflacaoMensal.csv')

    #Criando um novo campo:
inflação['Dcerta'] = inflação['Ano'] + (inflação['Mês'] / 12)

     #Execução do gráfico: 
import matplotlib.pyplot as plt
plt.figure()

    #Editar cor da função e tipo da linha:
plt.plot(inflação['Dcerta'], inflação['Inflação'], color='orangered', linestyle='-')

    #Editando o eixo da coordenada, abcissa eo nome do gráfico:
plt.xlabel('Anos')
plt.ylabel('Inflação Mensal em %')
plt.title('Inflação durante 1944 e 2019')

    #Para vizualização do gráfico:
plt.grid()
plt.show ()     
print(  )
    #Maior taxa de inflação mensal foi em:
x= inflação.tail(560)
taxa= inflação.sort_values(['Inflação', 'Mês'])
print('No mês', inflação['Mês'].values[1],'(Março) do ano', inflação['Ano'].values[560],'foi apresentado', inflação['Inflação'].values[553], '% de inflação')

print(  )

#Atividade 3- Mostre quais são os 10 programas mais vistos 
#E em qual mês do ano foi assistido mais programas   
   
     #Importar tabela e dados:
import pandas as pd
date = pd.read_csv('netflix.csv')

date['Categoria'] = 'Filme'
date['Categoria'][date['Title'].str.contains(": Temporada|: Stranger|: Parte")] = 'Série'  
date['Programa'] = date['Title']  
date[['Programa','Episódio']] = date[date['Categoria']=='Série']['Title'].str.split(pat = ': Temporada|: Stranger Things|: Parte', expand = True, n = 1)   
date.loc[date['Categoria']=='Filme', 'Programa'] = date.loc[date['Categoria']=='Filme', 'Title']  
date = date.drop(columns = 'Title')

    #Mostrar os 10 mais assistidos:
p = date['Programa'].value_counts()
q = p.head(10)
print('Os 10 programas mais assistidos:')
print(q)
print(  )
    #Mês do ano que mais foi assistido programas:
date['Date']= pd.to_datetime(date['Date'],format = '%d/%m/%Y')
date = date.sort_values(['Date'])
print('Mês do ano mais assitido foi 7 (Julho):')
print(date['Date'].dt.month)
