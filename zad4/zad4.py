from zad4testy import runtests
from queue import Queue

# Piotr Śmiałek
# Szukam najkrótszej ścieżki od S do T za pomoca funkcji bfs_shortest_path
# która zwraca pred - tablice poprzednikow i distance - tablice odleglosci do wierzcholkow
# nastepnie odwzorowuje droge path z S do T. Mając juz najkrótszą drogę w tablicy path
# wywoluje funkcje find_edge, która sprawdza czy usunięcie krawędzi z path wydluza droge
# (krawędzie usuwam zaczynajac od strony T)
# Złożoność: O(2*(V+E))-najbardziej pesymistyczny przypadek



def bfs_shortest_path(G,s,t):
    queue = Queue()
    visited = [False] * len(G)
    queue.put(s) 
    visited[s] = True

    distance=[10**10]*len(G)
    pred=[-1]*len(G)
    distance[s]=0



    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True

                distance[v]=distance[u]+1
                pred[v]=u

                if v==t:
                    return pred,distance
    return None,None

def find_edge(G,s,t,edge):
    queue = Queue()
    visited = [False] * len(G)
    queue.put(s) 
    visited[s] = True

    v_1=edge[0]
    v_2=edge[1]
    pred=[-1]*len(G)
    distance=[10**10]*len(G)
    distance[s]=0

    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not ((u==v_1 and v==v_2) or (u==v_2 and v==v_1)):

                if not visited[v]:
                    queue.put(v)
                    visited[v] = True

                    distance[v]=distance[u]+1
                    pred[v]=u
                    if v==t:
                        return distance[t]
    return distance[t]


def longer( G, s, t ): 
    
    pred,distance=bfs_shortest_path(G,s,t)
    
    if pred==None and distance==None:
        return None

    temp=t

    path=[]
    path.append(t)
    while pred[temp]!=-1:
        path.append(pred[temp])
        temp=pred[temp]


    for i in range(len(path)-1):
        edge=(path[i],path[i+1])
        new_distance=find_edge(G,s,t,edge)
        if new_distance>distance[t]:
            return edge

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True)