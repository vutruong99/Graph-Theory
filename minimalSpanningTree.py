from random import randint

import numpy as np

data = np.loadtxt("matrix_gts.txt")

def vertciescheck(tree_vertices, min):
    chosen_vertex_start = 0
    chosen_vertex_end = 0
    min_vertex_start = 0
    min_vertex_end = 0
    for i in tree_vertices: # Check in
        for j in range(12):
            if data[i][j] != 0 and j not in tree_vertices:
                chosen_vertex_start = i
                chosen_vertex_end = j
                if data[chosen_vertex_start][chosen_vertex_end] <= min:
                    min = data[chosen_vertex_start][chosen_vertex_end]
                    min_vertex_start = chosen_vertex_start
                    min_vertex_end = chosen_vertex_end

    return min_vertex_start, min_vertex_end


def spanningtrees(matrix):
    vertices = np.arange(12)
    tree_vertices = np.array([vertices[randint(0, 12)]])  # V1 Visited vertices
    edges = np.array([]) #E1

    chosen_vertex_start = 0
    chosen_vertex_end = 0
    total = 0

    while 1:
        if(vertciescheck(tree_vertices, min)  != (0,0)):
            new_edge = np.array([])
            new_edge = np.append(new_edge, [vertciescheck(tree_vertices, min)])
            total = total + data[vertciescheck(tree_vertices,min)[0]][vertciescheck(tree_vertices,min)[1]]
            tree_vertices = np.append(tree_vertices, [vertciescheck(tree_vertices,min)[1]])
            edges = np.append(edges, [new_edge])
            print(tree_vertices)
        else: break
    return edges, total


min = 100000000000

print(spanningtrees(data))





