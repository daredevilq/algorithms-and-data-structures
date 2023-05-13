from zad3testy import runtests

# Piotr Śmiałek
# Najpierw doklejam do tablicy odwrocone slowa z tablicy T. 
# W wyniku czego powstaje mi tablica rozmiaru 2n, 
# gdzie n bylo pierwotnym rozmariem tablicy. Dzieki temu
# kolo siebie gromadze slowa rowowazne i nie musze uzywac dodatkowej petli for 
# zeby skakac po wyrazach
# Nastepnie sortuje tablice mergsortem po czym przechodze po tablicy 
# liczac wyrazy rownowazne. Uwzgledniam tez palindromy ktore wystapily 
# w tablicy wtedy ich liczba jest dwukrotnie mniejsza - dlatego zamiast +=1 dodaje +=0.5
# zlozonosc O(n +2nlog2n) 
 

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2

        left=arr[:mid]
        right=arr[mid:]

        mergeSort(left)

        mergeSort(right)


        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1


        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
                                                            
        while j<len(right):                         
            arr[k]=right[j]                 
            j+=1                
            k+=1                    


def strong_string(T):

    for i in range(len(T)):
        temp=T[i]
        T.append(temp[::-1])

    mergeSort(T)
    
    cnt=1
    max_cnt=-1
    flag=True
    for i in range(1,len(T)):
        temp=T[i-1]
        if flag:
            if temp==temp[::-1]:
               cnt=0.5
            else:
                cnt=1

        if T[i-1]==T[i]:
            flag=False
            if temp==temp[::-1]:
                cnt+=0.5
            else:
                cnt+=1
        else:
            if cnt>max_cnt:
                max_cnt=cnt
            flag=True

    return int(max_cnt)
    
    

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
