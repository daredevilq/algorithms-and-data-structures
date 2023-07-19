from zad8testy import runtests
from queue import PriorityQueue
def is_valid(T,y,x):
    if x>=0 and y>=0 and x<len(T[0]) and y<len(T) and T[y][x]!=0:
        return True
    return False


def dfs_sum(T,y,x,moves):
    oil_amount=0
    column=x
    def dfs(y,x,moves):
        nonlocal oil_amount
        oil_amount+=T[y][x]
        T[y][x]=0
        for dy,dx in moves:
            if is_valid(T,y+dy,x+dx):
                dfs(y+dy,x+dx,moves)

    dfs(y,x,moves)
    T[0][column]=oil_amount

def plan(T):
    moves=[(1,0),(0,1),(0,-1),(-1,0)]
    for i in range(len(T[0])):
        if T[0][i]!=0:
            dfs_sum(T,0,i,moves)

    if T[0][0]==2:
        for i in T:
            print(i)
    stops_list=[]
    curr_oil=0
    best_oil_stop=PriorityQueue()
    stops_counter=0
    for i in range(len(T[0])-1):
        if T[0][i]!=0:
            best_oil_stop.put(-1*T[0][i])
        if curr_oil==0:
            curr_oil+=(-1*best_oil_stop.get())
            stops_counter+=1
            stops_list.append(i)
        curr_oil-=1


    return stops_counter



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

