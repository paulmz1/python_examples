from math import hypot
from itertools import permutations


def default_distance(graph, a, b):
    return hypot(graph[a]['x'] - graph[b]['x'], graph[a]['y'] - graph[b]['y'])


def sum_distance(route, graph, distance_function):
    dist = 0

    r = route + (route[0],)
    for i in range(len(r) - 1):
        dist += distance_function(graph, r[i], r[i+1])

    return dist


# Returns partial solutions. LAst is the optimal solution
def solve_itr(graph, distance_function=default_distance):
    perm = permutations(range(len(graph)))
    shortest_dist = None

    for route in perm:
        dist = sum_distance(route, graph, distance_function)

        if shortest_dist is None or dist < shortest_dist:
            shortest_dist = dist
            yield shortest_dist, list(route)


def solve(points, distance_function):
    *_, last = solve_itr(points, distance_function)
    return last
