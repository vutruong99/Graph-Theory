from random import randint

import numpy as np

data = np.loadtxt("matrix_gts.txt", dtype=int)

def vertciescheck(tree_vertices):
    chosen_vertice_start = 0
    chosen_vertice_end = 0
    for i in tree_vertices:
        count = 0
        for j in range(12):
            if data[i][j] != 0 and j not in tree_vertices:
                chosen_vertice_start = i
                chosen_vertice_end = j

                count = 1
                break;
        if count != 0: break
    return chosen_vertice_start, chosen_vertice_end

def spanningTrees(matrix):
    vertices = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
    tree_vertices = np.array([vertices[randint(0,12)]]) #v1
    edges = np.array([]) #E1

    chosen_vertice_start = 0
    chosen_vertice_end = 0

    while 1:
        if(vertciescheck(tree_vertices)  != (0,0)):
            new_edge = np.array([])
            new_edge = np.append(new_edge, [vertciescheck(tree_vertices)])
            tree_vertices = np.append(tree_vertices, [vertciescheck(tree_vertices)[1]])
            edges = np.append(edges, [new_edge])
            print(tree_vertices)
        else: break
    return edges

print(spanningTrees(data))





