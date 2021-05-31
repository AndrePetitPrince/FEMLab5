import numpy as np
import matplotlib.pyplot as plt

def plot_results(nodes, x):    
    u = nodes[:,1]
    
    plt.figure()
    plt.plot(u, x, 'm*')
    plt.show()