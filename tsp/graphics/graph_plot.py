import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def get_edge_labels(G, solution, pos):
    sol_pairs = {}
    s = solution[1] + [solution[1][0],]
    for i in range(len(s) - 1):
        sol_pairs[(s[i], s[i + 1])] = i

    edge_labels ={}
    for u, v, d in G.edges(data=True):
        if pos[u][0] > pos[v][0]:
            bottom_length = G.edges[(v, u, 0)]["weight"]
            step = sol_pairs.get((u, v), sol_pairs.get((v,u), None))
            step = '' if step is None else f'({step})'
            edge_labels[(u, v,)] = f'{d["weight"]}\n{step}\n{bottom_length}'

    return edge_labels


def plot(graph, solution, start=0):

    G = nx.from_numpy_matrix(np.array(graph), create_using=nx.MultiDiGraph())

    pos = nx.spring_layout(G)
    fig = plt.figure('Traveling Salesman')
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='pink', alpha=0.9,
            connectionstyle='arc3, rad = 0.05',
            labels={node: node+start for node in G.nodes()})

    edge_labels = get_edge_labels(G, solution, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.axis('off')
    fig.text(.05, .02, f'Distance={solution[0]}, Route={solution[1]}', ha='left')
    plt.show()

# https://stackoverflow.com/questions/22785849/drawing-multiple-edges-between-two-nodes-with-networkx/60678428#60678428
