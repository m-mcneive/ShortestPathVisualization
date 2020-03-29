from heapq import heappush
from heapq import heappop

def relax(W, u, v, D, P):
    inf = float('inf')
    d = D.get(u, inf) + W.getNeighbors(u[0], u[1])[v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True


def dijkstra(G, s):
    D, P, Q, S = {s: 0}, {}, [(0, s)], set()
    while Q:
        _, u = heappop(Q)
        if u in S:
            continue
        S.add(u)
        for v in G.getNeighbors(u[0], u[1]):
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))
    return D, P