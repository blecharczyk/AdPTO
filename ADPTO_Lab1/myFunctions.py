from dimacs import *
from itertools import *
import numpy as np
import myFunctions



def brut_force(G, E):
  for i in range(len(G)):
    for C in combinations(range(len(G)), i):
      if(isVC(E, set(C))):
        return(set(C))



#O(2^k)
def betterVC(G, k, S):
  E = edgeList(G);
  not_covered_edges = []
  for u, v in E:
    if u not in S and v not in S:
      not_covered_edges.append((u, v))

  if len(not_covered_edges) == 0:
    return S
  if k == 0:
    return None

  (u, v) = not_covered_edges[0]

  N = []
  for u in G[v].copy():
    N += [(u, v)]
    G[u].remove(v)
    G[v].remove(u)

  S1_tmp = S.copy()
  S1_tmp.add(v)
  S1 = betterVC(G, k - 1, S1_tmp)

  for (u, v) in N:
    G[u].add(v)
    G[v].add(u)

  N = []
  for v in G[u].copy():
    N += [(u, v)]
    G[u].remove(v)
    G[v].remove(u)

  S2_tmp = S.copy()
  S2_tmp.add(u)


  S2 = betterVC(G, k - 1, S2_tmp)


  for(u, v) in N:
    G[u].add(v)
    G[v].add(u)

  if S1:
    return S1
  else:
    return S2