import numpy as np
import matplotlib.pyplot as plt
from geo_plot import *

def rysuj_rozwiazanie(nodes, elements, WB, u):
    geo_plot(nodes, elements, WB)
    x = nodes[:,1]
    y = u

    plt.plot(x, y, '*m')
    plt.show()