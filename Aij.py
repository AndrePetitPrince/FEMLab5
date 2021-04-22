import numpy as np

def Aij(dphi1, dphi2, c, phi1, phi2):
    
    #Parametry :
    #dphi1 , dphi2 - pochodne funkcji ksztaltu zwiazanych z i-tym oraz j- tym wezlem
    #c
    #phi1
    #phi2

    #Zwraca :
    #wyrazenie lambda bedace funkcja podcalkowa A_ij
    #Aij =
    return lambda x: -dphi1(x) * dphi2(x) + c * phi1(x) * phi2(x)