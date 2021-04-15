import numpy as np
import matplotlib.pyplot as plt

def geo_plot(nodes, elements, n):
    zeros = np.zeros(n)
    l1 = plt.plot(nodes[:,1],zeros)
    for i in range(0, n, 1):
        plt.text(nodes[i,1], -0.01, str(i+1))
        plt.text(nodes[i,1], 0, "|")
    for i in range(0, n-1, 1):
        plt.text(nodes[i+1,1]/2+nodes[i,1]/2, 0.005 ,str(i+1))
    plt.show()