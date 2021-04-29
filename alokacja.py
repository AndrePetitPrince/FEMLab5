import numpy as np

def alokacja ( n):

#Parametry :
#n - rozmiar macierzy A ( nxn ) i wektora b ( nx1)
#Zwraca :
#A,b - tablice zer o rozmiarach odpowiednio nxn oraz nx1

    A = np.zeros([n,n])
    b = np.zeros([n,1])
    return A,b