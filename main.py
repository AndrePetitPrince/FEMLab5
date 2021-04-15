import numpy as np
import matplotlib.pyplot as plt
from init_params import *
from def_params_geo_fiz import *
from gen_geo_tab import *
from geo_plot import *

# ##############################################################################################
# # # # # PRE - PROCESSING # # # # #
## 1(a) inicjalizacja parametrow sterujacych programem CZESC 1
#[ parametry_sterujace ] = inicjalizacja_parametrow_sterujacych ( ... ) ;

#[c, f] = init_params()
#print("c: ", c)
#print("f: ", f)

c = 0;
f = 0;

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
print(elementy)


## 1(d) prezentacja geometrii zagadnienia CZESC 2
#rysuj_geometrie (WEZLY , ELEMENTY , WAR_BRZEGOWE ) ;

geo_plot(wezly, elementy, n)


'''
# 1(e) utworzenie macierzy wypelnionych zerami CZESC 3
[A,b] = alokacja_pamieci_na_zmienne_globalne ( liczba_wezlow ) ;

## 2(a) CZESC 3
[ lokalne_fun_ksztaltu , pochodne_lokalnych_fun_ksztaltu ] = definicja_funkcji_ksztaltu ( ... ) ;
# # # # # PROCESSING # # # # #
for k = 1: liczba_elementow_skonczonych

## 2(b) CZESC 4
[ nr_glob_elem , nr_glob_wezlow_elem , wspolrzedne_wezlow , jakobian ] =
zgromadzenie_informacji_dotyczacych_elementu (k, WEZLY , ELEMENTY , ...) ;
M = obliczenie_lokalnej_macierzy_opisujacej_element ( ) ;

## 2(c) CZESC 5
A = agregacja_macierzy_lokalnej_w_macierzy_globalnej (M, nr_glob_wezlow_elem , ...) ;
b = obliczanie_elementow_wektora_prawej_strony ( ) ;
end # for k = 1: liczba_elementow_skonczonych






## 2(d) CZESC 6
[A, b] = uwzglednienie_warunkow_brzegowych ( WAR_BRZEGOWE , ... ) ;

## 2(e) CZESC 7
a = rozwiazanie_url (A,b)
# # # # # POST - PROCESSING # # # # #

## 3(a) obrobka_wynikow ???? CZESC 8

## 3(b) prezentacja graficzna rozwiazania
rysuj_rozwiazanie (WEZLY , ELEMENTY , a)
# ##############################################################################################
'''