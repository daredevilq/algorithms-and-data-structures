from math import inf
from queue import PriorityQueue



def relaxation(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def spacetravel( n, E, S, a, b ):
    

    G= [[] for _ in range(n)]

    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
        if i+1<len(S):
            G[S[i]].append((S[i+1],0))
            G[S[i+1]].append((S[i],0))
          

    queue = PriorityQueue()
    queue.put((0, a))
    parent = [None] * len(G)
    distance = [inf] * len(G)
    visited = [False] * len(G)
    distance[a] = 0
    while not queue.empty():
        dist,u= queue.get()
        for v in G[u]:
            if not visited[v[0]] and relaxation(u, v, distance, parent):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    
    if distance[b]==inf:
        return None
    else:
        return distance[b]


E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7


print(spacetravel(n,E,S,a,b))





    
