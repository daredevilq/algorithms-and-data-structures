def is_valid(L,x_next,y_next):
    if x_next>=0 and y_next>=0 and x_next<len(L) and y_next<len(L) and L[y_next][x_next]=='.':
        return True
    return False

def maze10( L ):
    n=len(L)
    max_dist=0
    visited=[[False]*n for _ in range(n)]
    memo=[[0]*n for _ in range(n)]

    def maze_rec(L,x_current,y_current,x_dest,y_dest):
        if memo[y_current][x_current]!=0:
            return memo[y_current][x_current]
        
        if x_current==x_dest and y_current==y_dest:
            return 0
        visited[y_current][x_current]=True
        if is_valid(L,x_current+1,y_current):
            right= 1 + maze_rec(L,x_current+1,y_current,x_dest,y_dest)

        if is_valid(L,x_current,y_current+1):
            down = 1 + maze_rec(L,x_current,y_current+1,x_dest,y_dest)

        if is_valid(L,x_current,y_current-1):
            up = 1 + maze_rec(L,x_current,y_current-1,x_dest,y_dest)
       
        memo[x_current][y_current]=max(right,up,down)
        visited[y_current][x_current]=False
        return memo

    maze_rec(L,0,0,n-1,n-1)
    print(memo)


    n=len(L)
    if L[0][0]=="#" or L[n-1][n-1]=="#":
        return -1
    
    dp=[[-1]*(n) for _ in range(n)]
    colum_down=[0]*(n)
    colum_up=[-1]*(n)
    dp[0][0]=0


    for i in range(n):

        for j in range(1,n):
            if L[j][i]!="#" and colum_down[j-1]!=-1:
                colum_down[j]=colum_down[j-1]+1
            elif L[j][i]!="#" and colum_down[j-1]==-1 and dp[j][i-1]!=-1:
                continue
            else:
                colum_down[j]=-1

        if i!=0:
            for j in range(n-2,-1,-1):
                if L[j][i]!="#" and L[j+1][i-1]!=-1:
                    colum_up[j]=1+colum_up[j+1]
                else:
                    colum_up[j]=-1
        

        for j in range(n):
            temp=max(colum_down[j],colum_up[j])
            if temp==-1 or L[j][i]=="#":
                colum_down[j]=-1
                colum_up[j]=-1
                dp[j][i]=-1
            else:
                dp[j][i]=temp   
                colum_down[j]=1+temp
                colum_up[j]=1+temp
    if dp[n-1][n-1]==35:
        for i in L:
            print(i)

    return dp[n-1][n-1]
    


def maze_second( L ):
    n=len(L)
    if L[0][0]=="#" or L[n-1][n-1]=="#":
        return -1
    #dp=[[[-1]*(n+1) for _ in range(n+2)] for _ in range(3)]
    dp=[[-1]*(n) for _ in range(n)]
    colum_down=[0]*(n)
    colum_up=[0]*(n)
    dp[0][0]=0
    print("TO JEST N: ",n)
    print(len(L))
    for i in dp:
        print(i)
    print()

    for i in range(n-1):
        print()
        print("pre down ",colum_down,i)
        print("pre up ",colum_up,i)
        print()

        for j in range(1,n):
            if L[j][i]!="#" and colum_down[j-1]!=-1:
                colum_down[j]=colum_down[j-1]+1
            elif L[j][i]!="#" and colum_down[j-1]==-1 and dp[j][i-1]!=-1:
                continue
            else:
                colum_down[j]=-1

        if i!=0:
            for j in range(n-2,-1,-1):
                if L[j][i]=="#":
                    colum_up[j]=-1

                if L[j][i]!="#" and colum_down[j+1]!=-1:
                    colum_down[j]=colum_down[j+1]+1
                elif L[j][i]!="#" and colum_down[j+1]==-1 and dp[j][i-1]!=-1:
                    continue
                else:
                    colum_down[j]=-1
        
        print()
        print("post down ",colum_down,i)
        print("post up ",colum_up,i)
        print()
        for j in range(n):
            temp=max(colum_down[j],colum_up[j])
            if temp==-1 or L[j][i]=="#":
                colum_down[j]=-1
                colum_up[j]=-1
                dp[j][i]=-1
                dp[j][i+1]=-1
            else:
                dp[j][i]=temp
                dp[j][i+1]=temp+1   
                colum_down[j]=1+temp
                colum_up[j]=1+temp

        print("dp: ")
        for i in dp:
            print(i)
        print()
        print(dp[n-1][n-1])
        print("down ",colum_down,i)
        print("up ",colum_up,i)



def maze( L ):
    n=len(L)
    if L[0][0]=="#" or L[n-1][n-1]=="#":
        return -1
    
    dp=[[-1]*(n) for _ in range(n)]
    colum_down=[0]*(n)
    colum_up=[-1]*(n)
    dp[0][0]=0


    for i in range(n):
        print()
        print("pre down ",colum_down,i)
        print("pre up ",colum_up,i)
        print()

        for j in range(1,n):
            if i!=0:
                if L[j][i]!="#":
                    if colum_down[j-1]!=-1:
                        colum_down[j]=max(colum_down[j-1]+1,dp[j][i])
                    else:
                        colum_down[j]=dp[j][i]
                else:
                    colum_down[j]=-1
                
            else:
                if L[j][i]!="#" and colum_down[j-1]!=-1:
                    colum_down[j]=colum_down[j-1]+1
                else:
                    colum_down[j]=-1

        if i!=0:
            for j in range(n-2,-1,-1):
                if L[j][i]!="#":
                    if colum_up[j+1]!=-1:
                        colum_up[j]=max(dp[j][i],colum_up[j+1]+1)
                    else:
                        colum_up[j]=max(-1,dp[j][i])
                else:
                    colum_up[j]=-1

        print()
        print("post down ",colum_down,i)
        print("post up ",colum_up,i)
        print()

        for j in range(n):
            dp[j][i]=max(dp[j][i],colum_down[j],colum_up[j])
            if i<n-1:    
                if dp[j][i]==-1 or L[j][i+1]=="#":
                    dp[j][i+1]=-1
                    colum_down[j]=-1
                    colum_up[j]=-1
                
                else:
                    dp[j][i+1]=dp[j][i]+1
                    colum_down[j]=dp[j][i]+1
                    colum_up[j]=dp[j][i]+1

        print("dp: ")
        for i in dp:
            print(i)
        print()
        print(dp[n-1][n-1])




L2 = ['....', '..#.', '..#.', '....']
L3 = ['......', '#..#..', '.#..#.', '##..#.', '......', '......']
L=['....#...##',     
'...#....##',
'#.........',
'.......#..',
'.......##.',
'...#....#.',
'#....#....',
'##.....#.#',
'..........',
'......#...']


maze(L3)
#print(maze_copy(L))