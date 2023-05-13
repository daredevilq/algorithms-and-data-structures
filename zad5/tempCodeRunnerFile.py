    k=len(S)
    tab=[]
    for i in range(k):
        for j in range(i+1,k):
            tab.append((S[i],S[j],0))

    G= [[] for _ in range(n)]