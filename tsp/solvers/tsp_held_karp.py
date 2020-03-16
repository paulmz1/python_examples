# https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm#Recursive_formulation
def solve(graph, distance_function):

    def c(j, k):
        return distance_function(graph, j, k)

    def g(x: int, S: set) -> (int, list):
        return min([(c(x, s) + r, [s] + path) for s, (r, path) in
                    [(s, g(s, S - {s})) for s in S]],
                   key=lambda k: k[0]) if S else (c(x, 0), [])

    d, p = g(0, set(range(1, len(graph))))
    return d, [0] + p


'''

def c(j, k):
    return graph[j - 1][k - 1]

def g(x: int, S: set) -> (int, list):
    if S:
        mn, p = None, None
        for s in S:
            r = g(s, S - {s})
            d = c(x,s) + r[0]
            if mn is None or d < mn:
                mn = d
                p = [s] + r[1]
        return mn, p
    else:
        return c(x, 1), []
        

print(g(2, {}))
print(g(3, {}))
print(g(4, {}))
print(g(3, {2}))
print(g(1, {2, 3, 4})) # 1 → 3 → 4 → 2 → 1


'''