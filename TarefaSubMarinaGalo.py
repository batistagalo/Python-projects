"""
Tarefa Substitutiva de BCC

@author: Marina
"""

import numpy as np
import matplotlib.pyplot as plt

'''Deseja-se saber a taxa β da população saudável e não imunizada deve ser 
vacinada por dia para que o número de mortos devido à doença não ultrapasse 10 
em um ano. E faça o gráfico de 0 a 364 dias da população de cada um dos grupos 
com o valor de β encontrado.

Em que α, β, γ e δ são parâmetros reais entre 0 e 1:

α: taxa de contaminação da população saudável a cada dia.
β: taxa de população não infectada que é vacinada por dia.
γ: taxa da população infectada que se cura da doença e passa a ficar imunizada.
δ: taxa da população infectada que morre devido à doença.
N: número de novos habitantes.'''

DT=  np.arange(0,365,1)
α= 0.002
β= 0.01
γ= 0.15
δ= 0.00005
N= 3
P= np.ones(len(DT))
I= np.ones(len(DT))
C= np.ones(len(DT))
M= np.ones(len(DT))

P[0]= 10000
M[0]= 9

for k in range(1, len(DT),1):
    #A população saudável não imunizada P varia a cada dia com:
    P[k]= P[k-1]-α*P[k-1]-β*P[k-1]+N  
    #A população infectada I varia a cada dia com:
    I[k]= I[k-1]+α*P[k-1]-γ*I[k-1]- δ*I[k-1]
    #A população imunizada C varia a cada dia com:
    C[k]= C[k-1]+β*P[k-1]+γ*I[k-1]
    #O número de mortes M devido à doença varia com:
    M[k]= M[k-1]+ δ*I[k-1]

'''Para saber saber a taxa β da população saudável e não imunizada deve ser 
vacinada por dia para que o número de mortos devido à doença não ultrapasse 
10 em um ano.'''

m= np.max(M)
PontoMáximoDeMortesPorAno= np.logical_not(m>=10)
'''Retorna True se m é menor que 10 e False se m é maior ou igual a 10.
    Parâmetro:
    -----------------------------
    P[0]: float
        número float no qual representa a população saudável não imunizada que varia a cada dia
    m: float
       número float no qual representa o número de mortes M devido à doenças e será feita a verificação.
       
    Obs.: para fazer a verificação basta mudar o β (taxa de população não infectada que é vacinada por dia);
    Retorna:
    ----------------------------
    PontoMáximoDeMortesPorAno: boolean printado
         True indica que m está contido no intervalo. False indica que m não está contido no intervalo.
    '''     
print('Taxa β da população saudável e não imunizada deve ser vacinada por dia para que o número de mortos devido à doença não ultrapasse 10 em um ano:', PontoMáximoDeMortesPorAno)

#Para contruir o gráfico:
plt.figure()
plt.grid()
#Editar nome no eixo da coordenada, abcissa e o nome do gráfico:
plt.plot(DT, P, color='dodgerblue', linestyle='-', label='Saudável e não imunizada')
plt.plot(DT, I, color='orangered', linestyle='-', label='Infectada')
plt.plot(DT, C, color='green', linestyle='-', label='Imunizada')
plt.plot(DT, M, color='black', linestyle='-', label='Mortes')
plt.title('Gráfico da Imunização de população')
plt.xlabel('Dias do Ano')
plt.ylabel('Número de indivíduos')

#Para vizualização da legenda e do gráfico:
plt.legend()
plt.show