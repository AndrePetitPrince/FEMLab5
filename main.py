import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint
#from init_params import *
from def_params_geo_fiz import *
from gen_geo_tab  import *
from geo_plot  import *
from alokacja  import *
from funkcje_bazowe import *
from Aij import *
from rysuj_rozwiazanie import *

# ##############################################################################################
# # # # # PRE - PROCESSING # # # # #
## 1(a) inicjalizacja parametrow sterujacych programem CZESC 1
#[ parametry_sterujace ] = inicjalizacja_parametrow_sterujacych ( ... ) ;

#[c, f] = init_params()
#print("c: ", c)
#print("f: ", f)

c = 0
#f = lambda x: 0 #wymuszenie
f = 0

## 1(b) definicja parametrow fizycznych i geometrycznych obszaru , warunkow brzegowych CZESC 1
# - definicja przedzialu ,
# - liczba wezlow / elementow modelu w przypadku dyskretyzacji jednorodnej
# - zadanie funkcji wymuszajacej , parametrow rownania rozniczkowego
# - ...
#[ parametry_geom_i_fiz ] = definicja_parametrow_geom_i_fiz ( ... ) ;

#[x_0,x_R,twb_L,twb_R,wwb_L,wwb_R] = def_params_geo_fiz();
#print("x_0: ", x_0)
#print("x_R: ", x_R)
#print("twb_L: ", twb_L)
#print("twb_R: ", twb_R)
#print("wwb_L: ", wwb_L)
#print("wwb_R: ", wwb_R)

x_0 = 0;
x_R = 1;

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1


## 1(b/c) CZESC 1
#[ WEZLY , ELEMENTY , WAR_BRZEGOWE ] = definicja_zmiennych_przechowujacych_informacje_o_geometrii (parametry_geom_i_fiz , ... )
wezly = np.array([[1, 0],
                  [2, 1], 
                  [3, 0.5], 
                  [4, 0.75]])

elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [3, 3, 4]])

#n=input("Podaj liczbe wezlow: ")
n = 5

wezly, elementy = gen_geo_tab(x_0, x_R, n)
print(wezly)
print('\n')
print(elementy)
print('\n')

## 1(d) prezentacja geometrii zagadnienia CZESC 2
#rysuj_geometrie (WEZLY , ELEMENTY , WAR_BRZEGOWE ) ;

geo_plot(wezly, elementy, n)


# Processing
## 1(e) utworzenie macierzy wypelnionych zerami CZESC 3
#[A,b] = alokacja_pamieci_na_zmienne_globalne ( liczba_wezlow ) ;
[A,b] = alokacja(n)


### 2(a) CZESC 3
#[ lokalne_fun_ksztaltu , pochodne_lokalnych_fun_ksztaltu ] = definicja_funkcji_ksztaltu ( ... ) ;
stop_fun_b = 1
[phi, dphi] = funkcje_bazowe(stop_fun_b)

#xx = np.linspace(-1, 1, 101)
#plt.plot(xx, phi[0](xx), 'r')
#plt.plot(xx, phi[1](xx), 'g')
#plt.plot(xx, dphi[0](xx), 'b')
#plt.plot(xx, dphi[1](xx), 'c')

#for k = 1: liczba_elementow_skonczonych
### 2(b) CZESC 4
#[ nr_glob_elem , nr_glob_wezlow_elem , wspolrzedne_wezlow , jakobian ] =
#zgromadzenie_informacji_dotyczacych_elementu (k, WEZLY , ELEMENTY , ...) ;
#M = obliczenie_lokalnej_macierzy_opisujacej_element ( ) ;

liczba_elementow = np.shape(elementy)[0]

for ee in np.arange(0, liczba_elementow):
    
    elem_ind_wier = ee
    elem_glob_ind = elementy[ee, 0]
    elem_wezel_1 = elementy[ee, 1]
    elem_wezel_2 = elementy[ee, 2]

    glob_ind_wezlow = np.array([elem_wezel_1, elem_wezel_2])
    print(glob_ind_wezlow)
    print('\n')

    x_a = wezly[elem_wezel_1-1,1]
    x_b = wezly[elem_wezel_2-1,1]

    J = (x_b - x_a)/2

    Ml = np.zeros([stop_fun_b+1, stop_fun_b+1])

    m=0; n=0;
    Ml[m,n] = J * spint.quad(Aij(dphi[n], dphi[m], c, phi[n], phi[m]), -1, 1)[0]
    
    m=0; n=1;
    Ml[m,n] = J * spint.quad(Aij(dphi[n], dphi[m], c, phi[n], phi[m]), -1, 1)[0]

    m=1; n=0;
    Ml[m,n] = J * spint.quad(Aij(dphi[n], dphi[m], c, phi[n], phi[m]), -1, 1)[0]

    m=1; n=1;
    Ml[m,n] = J * spint.quad(Aij(dphi[n], dphi[m], c, phi[n], phi[m]), -1, 1)[0]

    A[np._ix(glob_ind_wezlow - 1, glob_ind_wezlow - 1)] = A[np._ix(glob_ind_wezlow - 1, glob_ind_wezlow - 1)] + Ml

    print(Ml)
    print('\n')

    print(A)
    print('\n')

    if WB[0]['typ'] == 'D':
        ind_wezla = WB[0]['ind']
        wart_war_brzeg = WB[0]['wartosc']

        iwp = ind_wezla - 1 #indeks wezla w tabeli Pythona

        D = 10 ** 14

        temp = A[iwp,iwp]
        A[iwp,iwp] = temp * D
        b[iwp]     = temp * D * wart_war_brzeg

    if WB[1]['typ'] == 'D':
        ind_wezla = WB[1]['ind']
        wart_war_brzeg = WB[1]['wartosc']

        iwp = ind_wezla - 1 #indeks wezla w tabeli Pythona

        D = 10 ** 14

        temp = A[iwp,iwp]
        A[iwp,iwp] = temp * D
        b[iwp]     = temp * D * wart_war_brzeg

    if WB[0]['typ'] == 'N':
        print('Jeszcze nie zaimplementowano')
    
    if WB[1]['typ'] == 'N':
        print('Jeszcze nie zaimplementowano')

    x = np.linalg.solve(A,b)
    print(x)

    rysuj_rozwiazanie(wezly, elementy, WB, x)
### 2(c) CZESC 5
#A = agregacja_macierzy_lokalnej_w_macierzy_globalnej (M, nr_glob_wezlow_elem , ...) ;
#b = obliczanie_elementow_wektora_prawej_strony ( ) ;
#end # for k = 1: liczba_elementow_skonczonych

### 2(d) CZESC 6
#[A, b] = uwzglednienie_warunkow_brzegowych ( WAR_BRZEGOWE , ... ) ;

### 2(e) CZESC 7
#a = rozwiazanie_url (A,b)
## # # # # POST - PROCESSING # # # # #

### 3(a) obrobka_wynikow ???? CZESC 8

### 3(b) prezentacja graficzna rozwiazania
#rysuj_rozwiazanie (WEZLY , ELEMENTY , a)
## ##############################################################################################
