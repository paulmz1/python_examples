from tsp.solvers.tsp_brute_force import solve as solve_brute_force
from tsp.solvers.tsp_held_karp import solve as solve_held_karp
from tsp.graphics.graph_plot import plot

graph1 = [
    [0, 2, 9, 10],
    [1, 0,  6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0],
]

graph2 = [
    [0, 2, 9, 10, 5 ],
    [1, 0,  6, 4, 13],
    [15, 14, 0, 8, 7],
    [6, 3, 20, 0, 11],
    [6, 3, 12, 19, 0]
]

graph3 = [
    [0, 49, 34, 96, 74],
    [49,  0, 10, 94, 43],
    [34, 10,  0, 21,  6],
    [96, 94, 21,  0, 70],
    [74, 43,  6, 70,  0]
]

# Set graphs and solver
solver = solve_held_karp # = solve_held_karp or solve_brute_force
graph = graph1 # = graph1, graph2 or graph3

solution = solver(graph, lambda g, j, k: g[j][k])
print(solution)
plot(graph, solution)





