"""
Tarefa 8 - BCC

Marina Galo
"""
# Atividade 1 - Calcular o IMC para determinada variável e 
# Mostrar juntamente a classificação do Índice de Massa Copórea

print('Atividade 1:')

import numpy as np

# letra A - Sendo massa igual a 52 Kg e altura 1.58 metros, temos:

    # Fórmula e variável utiliada utilizada:
m= 52
h= 1.58
i = m/ (h**2)
i2= np.ceil(i)

    # Classificação utilizada:
if i2 < 17 :
    print(i2, 'Kg/mª','= IMC Muito abaixo do peso')
else:
    if 17 < i2 <= 25:
        print(i2, 'Kg/mª','= IMC Abaixo do peso')
    else:
        print(i2, 'Kg/mª','= IMC Pesso normal') 
 
# letra B - Sendo massa igual a 83 Kg e altura 1.75 metros, temos:
        
    # Fórmula e variável utiliada utilizada:
m= 83
h= 1.75
i= m/ (h**2)
i3= np.floor(i)

    # Classificação utilizada:
if 17 < i3 <= 25:
    print( i3, 'Kg/mª','= IMC Pesso normal')
else:
    if 30 > i3 > 25:
        print(i3, 'Kg/mª','= IMC Acima do peso')
    else:
        print(i3, 'Kg/mª','= IMC Obesidade Grau I') 

# Letra C - Sendo massa igual a 60 Kg e altura 1.52 metros, temos:
        
    # Fórmula e variável utiliada utilizada:
m= 60
h= 1.52
i= m/ (h**2)
i4= np.ceil(i)

    # Classificação utilizada:
if 17 < i4 <= 25:
    print(i4, 'Kg/mª','= IMC Peso normal')
else:
    print(i4,'Kg/mª','= IMC Acima do peso')
    
print(  )

# Atividade 2 - Gere o gráfico de A(x) em função de x para 0 ⩽x⩽8.
    
#Determine a concentração x do íon de hidrônio que resulta em solução saturada 
#(i.e., com acidez nula). Acrescente uma instrução que gere um ponto vermelho 
#no gráfico correspondente à saturação nula da solução.

print('Atividade 2:')

    #Variação do tempo (eixo x) e vizualização do vetor utilizado:
x= np.arange(0 , 9, 1)
print('Intervalo da concentração de íons hidrônio:', x)

    #Fórmula e variável utilizada:
A= ((x**3)+ 3*(x**2)-(54))

     #Execução do gráfico (eixo y)
import matplotlib.pyplot as plt
plt.figure()

    #Marcação correspondente à acidez nula da solução (ponto vermelho):
u= x[A==0]
g= 0
m= np.min(x)
print('Atinge a acidez nula no ponto',u, 'de concentração de íon de hidrônio')

    #Editar cor da função e tipo da linha:
plt.plot (x,A, color= 'black', linestyle = ':', marker = '.')
plt.plot(u, g, color='red', marker= '.')

     #Editar nome no eixo da coordenada, abcissa e o nome do gráfico:
plt.xlabel('Concentração de íon de hidrônio')
plt.ylabel('Acidez do Ácido Clorídrico')
plt.title(' Gráfico da acidez de uma solução de hidróxido de magnésio em ácido clorídrico')

     #Para vizualização do gráfico:
plt.grid()
plt.show ()

print(   )

# Atividade 3- Fazer o gráfico:
x1= np.arange(-10, 11, 1)
f= np.abs(x1-2)+ np.abs(2*x1+1) -x1-6

print('Atividade 3:')

     #Execução do gráfico (eixo y)
import matplotlib.pyplot as plt
plt.figure()

    #Para valor de f(x)>0 e x>0:
p= np.logical_and(f>0, x1>0)
print('Valores não negativos=',p)
    #Para oter o número verdadeiro:
s= x1[p == True]
print( 'Destes verdadeiros, o número que satifaz a função =', np.min(s))

    #Editar cor da função e tipo da linha:
plt.plot (x1,f, color= 'goldenrod', linestyle = '-', marker= 'd')

     #Editar nome no eixo da coordenada, abcissa e o nome do gráfico:
plt.xlabel('Valores de  x1')
plt.ylabel('Resultados da Função')
plt.title('Gráfico de uma função modular')

     #Para vizualização do gráfico:
plt.grid()
plt.show ()

print(   )

# Atividade 4- Fazer o gráfico:

print('Atividade 4:')

    #Não existe um número real que satisfaça f(y)=0
    #Entretanto 1.7 e -1.7 é o de y mais aproximado para zerar a função:

y= 1.7 
f1= (y**2)- np.sin(0.784*(y**2))-2
print('Em y=', y, ', temos o valor f(y)=',f1, 'mais aproximado do f(y)=0')
    #Pode também ser utilizado função piso (np.floor) para arredondamento de y para 0 

    #Vetores e função utiliados para construir o gráfico:
y2= np.arange(-2, 2.5, 0.5)
f2= (y2**2)- np.sin(0.784*(y2**2))-2
print('Valores de y substituídos na função:', y2)

    #Execução do gráfico (eixo y)
import matplotlib.pyplot as plt
plt.figure()
    
     #Editar nome no eixo da coordenada, abcissa e o nome do gráfico:
plt.xlabel('Números de y')
plt.ylabel('Resultados da Função')
plt.title('Gráfico de uma função do Segundo Grau')

    #Editar cor da função e tipo da linha:
plt.plot (y2,f2, color= 'darkred', linestyle = '--', marker= '.')

    #Para vizualização do gráfico:
plt.grid()
plt.show ()
