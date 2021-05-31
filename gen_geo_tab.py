import numpy as np
def gen_geo_tab(x_L,x_R,n_n):   
    
    #Macierz wezlow
    index_n = np.arange(1,n_n+1)
    x = np.linspace(x_L,x_R,n_n) ;        
    nodes = (np.block([[index_n], [x]])).T

    #Macierz elementow
    index_e = np.arange(1,n_n)
    e_begin = np.arange(1,n_n)
    e_end = np.arange(2,n_n+1)
    elements = (np.block( [[index_e], [e_begin], [e_end]] ) ).T
                    
    return nodes, elements