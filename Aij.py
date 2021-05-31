import numpy as np

def Aij(dphi1, dphi2, c, phi1, phi2):    
    return lambda x: -dphi1(x) * dphi2(x) + c * phi1(x) * phi2(x)