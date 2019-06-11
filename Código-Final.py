"""
Insper
Author: Diogo Nobre de Araujo Cintra
Graduated in Mechanical Engineering
Email: diogonac@al.insper.edu.br

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Constantes

c = 3516.912 #J/(Kg.K)

kw = 0.03825 #Condutividade térmica do ar (W/m.K)

u = 0.00002573 #Viscosidade dinâmica do fluido (N·s/m2)

visc = 0.00003447 #Viscosidade cinemática do fluido (m2/s)

d = 0.964 #densidade do fluido (kg/m3)

v = 13.39478744 #Velociade média do fluido (m/s)

Pr = 0.6974 #Número de Prandtl

m = [0.00632,0.1885,0.300] #massa de uma batata e duas porções diferentes de batata (kg)
A = [0.003042,0.024900, 0.029700] #área de cada "batata" (m2)
V = [0.00000648,0.000247,0.000324] #volume de cada "batata" (m3)



L = [] #lista das dimensões características
Re = [] #lista dos números de reynolds
Nu = [] #lista dos números de nusselt
h = [] #lista dos coeficientes de convecção térmica
i=0
y=0
while i<len(m):
    l=V[i]/A[i] #cálculo da dimensão característica
    i+=1
    L.append(l)
print(L)

for e in L:
    re = (d*v*e)/u #cálculo do número de reynolds
    Re.append(re)
print(Re)

for r in Re:
    nu = 0.037* r**(4/5) * Pr**(1/3) #cálculo do número de nusselt
    Nu.append(nu)
print(Nu)
    
while y<len(Nu):
    H = (Nu[y]*kw)/L[y] #cálculo do coeficiente de convecção térmica
    y+=1
    h.append(H)
print(h)   

Ta = 473.15 #Temperatura ambiente em Kelvin


Tb = (273.15 -18) #Temperatura inicial da batata


def derivada(Tb, t, m,h,A):
    dTdt=(1/(m*c))*h*A*(Ta-Tb)
    return dTdt

delta_t = 0.01
tempo = np.arange(0,1200,delta_t)
inicial = [Tb]
listaTempo = []
s = 0
z = 0
while s < 3 :
    solucao = odeint(derivada, inicial, tempo, args=(m[s],h[s],A[s]))
    solucao_celsius = []
    Tfinal = 0
    for k in solucao:
        e = k-273.15
        solucao_celsius.append(e)
    for z in range(len(tempo)):
        if solucao_celsius[z] < 160:
            Tfinal = tempo[z]
      
    listaTempo.append(Tfinal)
    plt.plot(tempo,solucao_celsius, label = ("m=%.3f Kg" % (m[s]))) 
    s+=1

            
print(listaTempo)
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura - Batata (Celsius)")
plt.title("Variação da temperatura da batata pelo tempo")
plt.legend()
plt.grid(True)
plt.show()

tempo_minuto = []
for t in listaTempo:
    tempo_minuto.append(t/60)

print(tempo_minuto)
tempo_validacao = [4,9.34,12]

plt.scatter(tempo_minuto,m, label = "modelo")
plt.scatter(tempo_validacao,m, label = "experimento")
plt.xlabel("Tempo (min)")
plt.ylabel("Massa - Batata (Kg)")
plt.title("Relação entre massa de batata e seu tempo de fritura")
plt.legend()
plt.grid(True)
plt.show()

