from tsp.solvers.tsp_brute_force import solve as solve_brute_force
from tsp.solvers.tsp_held_karp import solve as solve_held_karp
from tsp.graphics.graph_plot import plot
solvers = (solve_brute_force, solve_held_karp)

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
solver = solvers[1]
solution = solver(graph2, lambda g, j, k: g[j][k])
print(solution)
plot(graph2, solution)





