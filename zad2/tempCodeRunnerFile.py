
def snow(S):
    
    max_value=0
    for i in range(1,len(S)):
        if S[i]>max_value:
            max_value=S[i]
    
    heap_sort(S,max_value)

    counter=0
    days=0

    for i in range(len(S)-1,-1,-1):
        if S[i]-days<=0:
            return counter
        counter+=S[i]-days
        days+=1
    return counter
