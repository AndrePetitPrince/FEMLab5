import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint

from gen_geo_tab  import *
from geo_plot  import *
from allocation import *
from basis_functions import *
from Aij import *
from plot_results import *

#PRE-PROCESSING

#Parametry sterujace
c = 0 #wspolczynnik drgan wlasnych
f = lambda x: 0*x #wymuszenie
#f = 0        
     
#Reczna definicja wezlow    
wezly = np.array([[1, 0],
                  [2, 1], 
                  [3, 0.5], 
                  [4, 0.75]])
        
#Reczna definicja elementow   
elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [3, 3, 4]])

#Parametry geometryczne obszaru    
x_L = 0
x_R = 1
n_n = 15
        
#Automatyczne generowanie geometrii
wezly, elementy = gen_geo_tab(x_L, x_R, n_n)

print(wezly)
print('\n')
print(elementy)
print('\n')

#Parametry warunkow brzegowych
WB = [{"ind": 1,   "typ":'D', "wartosc":1}, 
      {"ind": n_n, "typ":'D', "wartosc":2}]

#Prezentacja graficzna problemu
geo_plot(wezly, elementy, n_n)

#Alokacja pamieci
A, b = allocation(n_n)

#Definicja funkcji bazowych i ich pochodnych
stop_fun_b = 1
phi, dphi = basis_functions(stop_fun_b)

xx = np.linspace(-1, 1, 101)
plt.figure()
plt.plot(xx, phi[0](xx), 'r')
plt.plot(xx, phi[1](xx), 'g')
plt.plot(xx, dphi[0](xx), 'b')
plt.plot(xx, dphi[1](xx), 'c')
plt.show

#PROCESSING

#Obliczanie macierzy lokalnej i agregacja wynikow w macierzy globalnej
liczba_elementow = np.shape(elementy)[0]
        
for ee in np.arange(0, liczba_elementow):
            
            elem_ind_wier = ee
            elem_glob_ind = elementy[ee, 0]
            elem_wezel_1 = elementy[ee, 1]
            elem_wezel_2 = elementy[ee, 2]
        
            glob_ind_wezlow = np.array([elem_wezel_1, elem_wezel_2])
            print(glob_ind_wezlow)
            print('\n')
        
            x_a = wezly[int(elem_wezel_1)-1,1]
            x_b = wezly[int(elem_wezel_2)-1,1]
        
            J = (x_b - x_a) / 2
        
            Ml = np.zeros([stop_fun_b + 1, stop_fun_b + 1])
        
            m=0; n=0;
            Ml[m,n] = J * spint.quad(Aij(dphi[m], dphi[n], c, phi[m], phi[n]), -1, 1)[0]
            
            m=0; n=1;
            Ml[m,n] = J * spint.quad(Aij(dphi[m], dphi[n], c, phi[m], phi[n]), -1, 1)[0]
        
            m=1; n=0;
            Ml[m,n] = J * spint.quad(Aij(dphi[m], dphi[n], c, phi[m], phi[n]), -1, 1)[0]
        
            m=1; n=1;
            Ml[m,n] = J * spint.quad(Aij(dphi[m], dphi[n], c, phi[m], phi[n]), -1, 1)[0]
        
            A[np.ix_(glob_ind_wezlow - 1, glob_ind_wezlow - 1)] = \
                A[np.ix_(glob_ind_wezlow - 1, glob_ind_wezlow - 1)] + Ml
        
            print(Ml)
            print('\n')
            
            print(A)
            print('\n')

#Wyliczenie wartosci macierzy z uwzglednieniem warunkow brzegowych
print(WB)
print('\n')

if WB[0]['typ'] == 'D':
    ind_wezla = WB[0]['ind']
    wart_war_brzeg = WB[0]['wartosc']

    iwp = ind_wezla - 1 #indeks wezla w tabeli Pythona

    wzmacniacz = 10 ** 14

    temp = A[iwp,iwp]
    A[iwp,iwp] = temp * wzmacniacz
    b[iwp]     = temp * wzmacniacz * wart_war_brzeg

if WB[1]['typ'] == 'D':
    ind_wezla = WB[1]['ind']
    wart_war_brzeg = WB[1]['wartosc']

    iwp = ind_wezla - 1 #indeks wezla w tabeli Pythona

    wzmacniacz = 10 ** 14

    temp = A[iwp,iwp]
    A[iwp,iwp] = temp * wzmacniacz
    b[iwp]     = temp * wzmacniacz * wart_war_brzeg

if WB[0]['typ'] == 'N':
    print('Jeszcze nie zaimplementowano')

if WB[1]['typ'] == 'N':
    print('Jeszcze nie zaimplementowano')
    
print(A)
print('\n')
print(b)
print('\n')
    
#Obliczenie wyniku 
x = np.linalg.solve(A,b)
print(x)

#Wyswietlenie graficznej interpretacji wyniku
plot_results(wezly, x)
