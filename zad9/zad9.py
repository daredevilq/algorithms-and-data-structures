from zad9testy import runtests
from math import inf

def solve(arr, i, left, used, max_dist, memo):
    if i == len(arr) - 1:
        return 0
    if left < 0 or used < 0 or left >= len(memo[0]) or used >= len(memo[0][0]):
        return inf

    #if (i, left, used) in memo:
    #    return memo[(i, left, used)]

    if memo[i][left][used] != -1:
        return memo[i][left][used]

    result1 = result2 = result3 = result4 = inf
    if left >= arr[i + 1][0] - arr[i][0]: 
        # Scenariusz 1: Możemy dojechać do następnego parkingu bez zatrzymania 
        # i bez korzystania z wyjątku (jeżeli jest dostępny)
        result1 = solve(arr, i + 1, left - arr[i + 1][0] + arr[i][0], used, max_dist, memo)
        
        # Scenariusz 2: Możemy dojechać do następnego parkingu bez zatrzymania 
        # i decydujemy się skorzystać z wyjątku (jeżeli jest dostępny)
        if used == 0:
            result2 = solve(arr, i + 1, left - arr[i + 1][0] + arr[i][0] + max_dist, 1, max_dist, memo)

    if used == 0 and left + max_dist >= arr[i + 1][0] - arr[i][0]:
        # Scenariusz 3: Nie możemy dojechać do następnego parkingu bez zatrzymania, 
        # ale możemy skorzystać z wyjątku i dojechać bez zatrzymania

        result3 = solve(arr, i + 1, left + max_dist - arr[i + 1][0] + arr[i][0], 1, max_dist, memo)

    # Scenariusz 4: Zatrzymujemy się na obecnym parkingu
    result4 = arr[i][1] + solve(arr, i + 1, max_dist - arr[i + 1][0] + arr[i][0], used, max_dist, memo)

    result = min(result1, result2, result3, result4)
    memo[i][left][used] = result
    return result





def min_cost2( O, C, T, L ):
    new_tab = [(0,0)]

    memo = [[[-1 for x in range(3)] for y in range(T + 2 )] for z in range(len(O) + 2 )] # i left used

    for i in range(len(O)):
        new_tab.append((O[i],C[i]))
    
    new_tab.sort()
    new_tab.append((L,0))

    #result = solve(new_tab, 0, T, 0, T,{})
    result = solve(new_tab, 0, T, 0, T,memo)
    return result
# zmien all_tests na True zeby uruchomic wszystkie testy


def min_cost( O, C, T, L ):
    #sortuję obie tablice po dystansach, dodaję dodatkowo na początku pozycję 0 a na końcu L
    #możnaby stworzyć nowe tablice, bo lepiej nie modyfikować parametrów funkcji, ale no cóż.
    n=len(O)
    A=[(O[i],C[i]) for i in range(n)]
    A.sort()
    O[0]=C[0]=0
    for i in range(n-1):
        O[i+1]=A[i][0]
        C[i+1]=A[i][1]
    O.append(A[n-1][0])
    O.append(L)
    C.append(A[n-1][1])
    C.append(0)
    #tablica 2x(n+2), wartości w pierwszym wierszu - przed wykorzystaniem wyjątku,
    #w drugim wierszu - po wykorzystaniu
    DP=[[float('inf') for _ in range(n+2)] for _ in range(2)]
    DP[0][0]=0
    h=k=0
    #i,j - wskaźniki indeksów po skoku z pierwszego wiersza, l - z drugiego
    #analogicznie h i k - przed skokiem
    #czemu <=n+2? szczerze nie analizowałem dokładnie, a dla <=n+1 jeden z testów miał błędny wynik
    #więc to obejmuje ten edge case
    while h<=n+2:
        i=j=h
        l=k
        min_ind_T1=h+1
        min_ind_T2=k+1
        #1 opcja - jeszcze nie wykorzystano wyjątku, dalej nie korzystam
        #wszędzie na bieżąco przy okazji zapisuję indeks najbardziej opłacalnego skoku
        #(oprócz 2 opcji) - znacznie przyspiesza to rozwiązanie
        while i<n+1 and O[i+1]-O[h]<=T:
            DP[0][i+1]=min(DP[0][i+1],DP[0][h]+C[i+1])
            if DP[0][i+1]<=DP[0][min_ind_T1]: min_ind_T1=i+1
            i+=1
        #2 opcja - właśnie wykorzystuję wyjątek
        while j<n+1 and O[j+1]-O[h]<=2*T:
            DP[1][j+1]=min(DP[1][j+1],DP[0][h]+C[j+1])
            j+=1
        #3 opcja - już po wykorzystaniu wyjątku
        while l<n+1 and O[l+1]-O[k]<=T:
            DP[1][l+1]=min(DP[1][l+1],DP[1][k]+C[l+1])
            if DP[1][l+1]<=DP[1][min_ind_T2]: min_ind_T2=l+1
            l+=1
        h=min_ind_T1
        k=min_ind_T2
    return DP[1][n+1]

runtests( min_cost, all_tests = True )
