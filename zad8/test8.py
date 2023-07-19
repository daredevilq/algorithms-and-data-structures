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
    moves=[(1,0),(0,1),(0,-1)]
    for i in range(len(T[0])):
        if T[0][i]!=0:
            dfs_sum(T,0,i,moves)

    for i in T:
        print(i)

    curr_oil=0
    best_oil_stop=PriorityQueue()
    stops_counter=0
    for i in range(len(T[0])-1):
        print("curr oil ",curr_oil,"  stops: ",stops_counter,"  i:",i)
        if T[0][i]!=0:
            best_oil_stop.put(-1*T[0][i])
        if curr_oil<=0:
            curr_oil+=(-1*best_oil_stop.get())
            stops_counter+=1
        
        curr_oil-=1


    return stops_counter

T=[[5, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 6, 4, 0, 0, 1],
   [0, 0, 0, 0, 0, 4],
   [0, 0, 6, 0, 10, 3],
   [0, 0, 7, 0, 11, 2]]

print(plan(T))