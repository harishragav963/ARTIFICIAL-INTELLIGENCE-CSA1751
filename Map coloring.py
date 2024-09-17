V = 4
graph = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
def isValid(v, color, c):  # check whether putting a color valid for v
    for i in range(V):
        if graph[v][i] and c == color[i]:
            return False
    return True
def mColoring(colors, color, vertex):
    if vertex == V:  # when all vertices are considered
        return True
    for col in range(1, colors + 1):
        if isValid(vertex, color,
                   col):  # check whether color col is valid or not
            color[vertex] = col
            if mColoring(colors, color, vertex + 1):
                return True  # go for additional vertices
            color[vertex] = 0
    return False  # when no colors can be assigned
colors = 3  # Number of colors
color = [0] * V  # make color matrix for each vertex
if not mColoring(
        colors, color,
        0):  # initially set to 0 and for Vertex 0 check graph coloring
    print("Solution does not exist.")
else:
    print("Assigned Colors are:")
    for i in range(V):
        print(color[i], end=" ")