from dimacs import *


def approx_with_2_factor(G):
    Edges = edgeList(G)
    G_cpy = G.copy()
    result = set()
    while not isVC(Edges, result):
        Edges2 = edgeList(G_cpy)
        u, v = Edges2[0]
        result.update({u, v})
        for i in G_cpy[v].copy():
            G_cpy[i].remove(v)
            G_cpy[v].remove(i)
        for i in G_cpy[u].copy():
            G_cpy[i].remove(u)
            G_cpy[u].remove(i)
    return result

def approx_log_n(G):
    Edges = edgeList(G)
    G_cpy = G.copy()
    result = set()
    while not isVC(Edges, result):
        v = G.index(max(G_cpy, key = len))
        result.add(v)
        for u in G_cpy[v].copy():
            G_cpy[u].remove(v)
            G_cpy[v].remove(u)
    return result
