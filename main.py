import numpy as np
import matplotlib.pyplot as plt

# ##############################################################################################
# # # # # PRE - PROCESSING # # # # #

def generujTabliceGeometrii(x_0, x_p, n):
    length = (x_p - x_0) / (n - 1)
    k = np.array([x_0, x_p])

    for i in range(1, n, 1):
        k = np.block([k, i * length + x_0])
    return k

## 1(a) inicjalizacja parametrow sterujacych programem CZESC 1
#[ parametry_sterujace ] = inicjalizacja_parametrow_sterujacych ( ... ) ;

## 1(b) definicja parametrow fizycznych i geometrycznych obszaru , warunkow brzegowych CZESC 1
# - definicja przedzialu ,
# - liczba wezlow / elementow modelu w przypadku dyskretyzacji jednorodnej
# - zadanie funkcji wymuszajacej , parametrow rownania rozniczkowego
# - ...
#[ parametry_geom_i_fiz ] = definicja_parametrow_geom_i_fiz ( ... ) ;
x_0=0;
x_1=1;

wezly = np.array([0, 1, 0.5, 0.75])

elementy = np.array([[1, 3],
                     [4, 2],
                     [3, 4]])

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1

## 1(b/c) CZESC 1
#[ WEZLY , ELEMENTY , WAR_BRZEGOWE ] = definicja_zmiennych_przechowujacych_informacje_o_geometrii (parametry_geom_i_fiz , ... )
print(generujTabliceGeometrii(1,2,5))

'''
## 1(d) prezentacja geometrii zagadnienia CZESC 2
rysuj_geometrie (WEZLY , ELEMENTY , WAR_BRZEGOWE ) ;

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