from zad7testy import runtests
# Piotr Śmiałek
# Tworze tablice dp 2-wymiarowa, gdzie dp[j][i] oznacza maksymalna droge od lewego 
# gornego rogu do punktu (j,i) poruszajac sie tylko we wskazanych 3kierunkach(prawo, dół, góra).
# Tworze również dwie tablice jednowymiarowe column_down i column_up.
# Dla kazdej kolumny i obliczam talbice column_down i column_up.
# wartosc column_down[j] oznacza czy da sie przejsc od elementu j-1 do elementu j w kolumnie i idac w dół.
# Odpowiednio dla column_up tylko ze w sprawdzam czy z dolu da sie przejsc w gore.
# column_down[j] / column_up[j] obliczany jest jako max wartosc z odpowiednio pola wyzej + 1, pola nizej + 1 i 
# wartosci dp[j-1][i] - (czyli po prostu przejscia z lewej do prawej)
# Ostatnia -trzecia petla for odpowiada za wpisanie wartosci do tablicy dp.
# Pod indeksem dp[j][i] wpisywana jest max wartosc z column_down[j] i column_up[j].
# Złożoność O(n^2) 

def maze( L ):
    n=len(L)
    if L[0][0]=="#" or L[n-1][n-1]=="#":
        return -1
    
    dp=[[-1]*(n) for _ in range(n)]
    column_down=[0]*(n)
    column_up=[-1]*(n)
    dp[0][0]=0

    for i in range(n):
        for j in range(1,n):
            if i!=0:
                if L[j][i]!="#":
                    if column_down[j-1]!=-1:
                        column_down[j]=max(column_down[j-1]+1,dp[j][i])
                    else:
                        column_down[j]=dp[j][i]
                else:
                    column_down[j]=-1            
            else:
                if L[j][i]!="#" and column_down[j-1]!=-1:
                    column_down[j]=column_down[j-1]+1
                else:
                    column_down[j]=-1

        if i!=0:
            for j in range(n-2,-1,-1):
                if L[j][i]!="#":
                    if column_up[j+1]!=-1:
                        column_up[j]=max(dp[j][i],column_up[j+1]+1)
                    else:
                        column_up[j]=max(-1,dp[j][i])
                else:
                    column_up[j]=-1

        for j in range(n):
            dp[j][i]=max(dp[j][i],column_down[j],column_up[j])
            if i<n-1:    
                if dp[j][i]==-1 or L[j][i+1]=="#":
                    dp[j][i+1]=-1
                    column_down[j]=-1
                    column_up[j]=-1
                
                else:
                    dp[j][i+1]=dp[j][i]+1
                    column_down[j]=dp[j][i]+1
                    column_up[j]=dp[j][i]+1


    return dp[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True)
 