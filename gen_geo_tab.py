import numpy as np
def gen_geo_tab(x_0, x_R, n):

    elem_length = (x_R - x_0) / (n - 1)
    nodes = np.zeros((n, 2))

    for nodes_index in range(0, n, 1):
        nodes[nodes_index, 0] = nodes_index + 1
        nodes[nodes_index, 1] = nodes_index * elem_length + x_0

    elements = np.zeros((n-1, 3))

    for elements_index in range(0, n-1, 1):
        elements[elements_index, 0] = elements_index + 1
        elements[elements_index, 1] = elements_index + 1
        elements[elements_index, 2] = elements_index + 2

    return nodes, elements