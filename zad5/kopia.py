from zad5testy import runtests
from queue import PriorityQueue
from math import inf

# Piotr Śmiałek
# Dane sprowadzam do macierzy sasiedztwa i dodaje polączenia pomiedzy
# wierzcholkami z S, ktore maja koszt 0.
# Nastepnie wywoluje algorytm Dijkstry do znalezienia najkrotszej sciezki.
# Zlozonosc O(S^2 + E + nlogn)



def relaxation(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def spacetravel( n, E, S, a, b ):
    

    k=len(S)
    tab=[]
    for i in range(k):
        for j in range(i+1,k):
            tab.append((S[i],S[j],0))

    G= [[] for _ in range(n)]

    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
        if i<len(tab):
            G[tab[i][0]].append((tab[i][1],tab[i][2]))
            G[tab[i][1]].append((tab[i][0],tab[i][2]))



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




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )