import numpy as np
import matplotlib.pyplot as plt

def geo_plot(nodes, elements, n_n):
    zeros = np.zeros(n_n)
    plt.figure()
    plt.plot(nodes[:,1],zeros)
    for i in np.arange(0,n_n):
        plt.text(nodes[i,1], -0.01, str(nodes[i,1]))
        plt.text(nodes[i,1], 0, "|", c="b")
        plt.text(nodes[i,1], 0.005, str(i+1), c="b")
    for i in np.arange(0,n_n - 1):
        plt.text(nodes[i+1,1]/2+nodes[i,1]/2, 0.01 ,str(i+1), c="r")
    plt.show()