"""
Tarefa 20 - BCC

@author: Marina
"""
import numpy as np
import matplotlib.pyplot as plt

'''Atividade 1- Sabe-se que inicialmente a população de coelhos em um 
ecossistema é de 1000 coelhos. Deseja-se saber quantas raposas são necessárias 
colocar inicialmente neste ecossistema para que a população de coelhos não 
ultrapasse 1500 e não fique abaixo de 500. Utilize o modelo de Lotka-Volterra para isso.'''

#Vetores para o cálculo das populações:
#Vetor com a quantidades de dias estipulada:
DT= np.arange(0,999,0.01) 
#Vetor para armazenar a quantidade de coelhos em sequência dos dias: 
C= np.ones(len(DT))
#Vetor para armazenar a quantidade de raposas em sequência dos dias: 
R= np.ones(len(DT))

#Constantes reais positivas utilizadas na fórmula:
α= 0.0001 # por dia
β= 0.00001 # 1/raposas dia 
γ= 0.00000009 # 1/coelhos dia 
δ= 0.00007 # 1 por dia 

#Estipulando a quantidade inicial de cada população:
#Dos coelhos:
C[0]= 1000 
#Das raposas:
R[0]= 13

#Modelo de Lotka-Volterra:
for i in range (1,len(DT)):
    C[i]= C[i-1]+α*C[i-1]-β*R[i-1]*C[i-1]
    R[i]= R[i-1]+γ*R[i-1]*C[i-1]-δ*R[i-1]
    
#Para que a população de coelhos não ultrapasse 1500 e não fique abaixo de 500:
c= np.max(C)
PontoMáximoDeCoelhos= np.logical_and(c>500, c<1500)
'''Retorna True se c é maior que 500 e menor que 1500 e False se c é menor que 500 ou maior que 1500.
    Parâmetro:
    -----------------------------
    R[0]: float
        número float no qual representa a população de raposas e variando este que indica a população de coelhos
    c: float
       número float no qual representa a população de coelhos e será feita a verificação.
       
    Obs.1: para fazer a verificação basta mudar o núemro de R[0] (número inicial de raposas);
    Obs.2: atráves de testes esse núero não pode ultrapassar 16 raposas, dentro das condições da popúlação de coelhos.
    
    Retorna:
    ----------------------------
    PontoMáximoDeCoelhos: boolean printado
         True indica que c está contido no intervalo. False indica que c não está contido no intervalo.
    '''     
print('População de coelhos não ultrapassa 1500 e também não está abaixo de 500:', PontoMáximoDeCoelhos)

#Para contruir o gráfico:
plt.figure()
plt.grid()
#Editar nome no eixo da coordenada, abcissa e o nome do gráfico:
plt.plot(DT, C, color='dodgerblue', linestyle='-', label='Coelhos')
plt.plot(DT, R, color='orange', linestyle='-', label='Raposas')
plt.title('Gráfico das populações de coelhos e raposas')
plt.xlabel('Dias da população')
plt.ylabel('Número de indivíduos')

#Para vizualização da legenda e do gráfico:
plt.legend()
plt.show