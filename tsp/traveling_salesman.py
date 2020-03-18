from tsp.solvers.tsp_brute_force import solve as solve_brute_force
from tsp.solvers.tsp_brute_force import sum_distance
from tsp.solvers.tsp_held_karp import solve as solve_held_karp
from tsp.graphics.graph_plot import plot
from timeit import default_timer as timer
import numpy as np
N = 4

graph1 = [
    [0, 2, 9, 10],
    [1, 0,  6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0],
]


def gen(n):
    np.random.seed(1)
    m = np.random.randint(100, size=(n, n))
    for i in range(n):
        m[i][i] = 0
    return m

# Set graphs and solver
solver = solve_held_karp  # = solve_held_karp or solve_brute_force
graph = gen(N)  # = graph1, graph2...

print(len(graph))
print(graph)
start = timer()
dist_fun = lambda g, j, k: g[j][k]
solution = solver(graph, dist_fun)
elapsed = timer() - start
print(f'Elapsed time = {elapsed}s')
print(solution)
assert solution[0] == sum_distance(tuple(solution[1]), graph, dist_fun)
if N < 10:
    plot(graph, solution + (elapsed,))
else:
    print("Not plotting for N > 9 due to a key error. May try to fix.")





