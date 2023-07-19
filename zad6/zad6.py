from zad6testy import runtests
from math import inf
from queue import Queue

# Piotr Śmiałek
# Probelm pracownikow i maszyn jest problemem znalezienia najliczniejszego 
# skojarzenia w grafie dwudzielnym. Do tego celu uzywam algorytmu Hopcrofta-Karpa
# da sie tez metoda forda-fulkersona poprzez stworzenie macierzy 2n+2 ale jest to 
# rozwiazanie duzo wolniejsze.
# pairU jest tablica par lewych wierzcholkow z prawymi wierzchoklami V( jesli nie ma pary: 0 )
# odpowiednio parV
# distance tablica - 0 dla braku polaczenia, inf dla polaczenia
# Wierzcholki dziele na dwie grupy lewy zbior - U i prawy - V
# dodaje do lewej strony wierzcholek pomocniczy ktory pomoze mi znalezc nowa sciezke, ktory jest polaczcony z wszystkimi pozostalymi wierzcholkami.
# bfs'em wyszykuje sciezek resuidalych (sciezek ktore maja na koncach nieprzydzielone wierzcholki)
# po znalezieniu sciezki resuidalnej uzywam dfs do wypelnienia tablic pairU i pairV 
# Zlozonosc: O(E*sqrt(V)) 


def bfs(M,pairsU,pairV,distance,n):
    queue=Queue()
    distance[0]=inf
    for u in range(1,n+1):
        if pairsU[u]==0:
            distance[u]=0
            queue.put(u)
        else:
            distance[u]=inf
    while not queue.empty():
        u=queue.get()
        if distance[u]!=inf:
            for v in M[u]:
                if distance[pairV[v]]==inf:
                    distance[pairV[v]]=distance[u]+1
                    queue.put(pairV[v])

    if distance[0]==inf:
        return False
    return True

def dfs(u,M,distance,pairsV,pairsU):
    if u==0:
        return True
    for v in M[u]:
        if distance[pairsV[v]]==distance[u]+1:
            if dfs(pairsV[v],M,distance,pairsV,pairsU):
                pairsV[v]=u
                pairsU[u]=v 
                return True
    distance[u]=inf
    return False

def hopcroft_algorithm(bipartite_graph):
    n=len(bipartite_graph)
    bipartite_graph.insert(0,[])
    distance=[0]*(n+1)
    pairsU=[0]*(n+1)
    pairsV=[0]*(n+1)
    no_matchings=0
 
    while bfs(bipartite_graph,pairsU,pairsV,distance,n):
        for u in range(1,n+1):
            if pairsU[u]==0 and dfs(u,bipartite_graph,distance,pairsV,pairsU):
                no_matchings+=1
    return no_matchings

def binworker( M ):
    return hopcroft_algorithm(M)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
