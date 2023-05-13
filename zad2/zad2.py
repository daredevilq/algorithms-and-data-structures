from zad2testy import runtests

#Piotr Śmiałek
#Funkcja sortuje za pomoca heapsort sortuje max(S) najwiekszych elementow i umieszcza je na koncu listy,
#pod indeksem S[len(S)-1] jest najwiekszy element. Nie trzeba sortowac calej listy poniewaz po znalezieniu maxiumum 
# w liscie S wiemy ze maksymalnie zebranie sniegu zajmie nam max(S) dni poniewaz reszta sie roztopi
#nastepnie przechodzimy petla zbierajac snieg w losowej kolejnosci(nie ma to znaczenia poniewaz stapianie sie sniegu jest liniowe)
#odejmujemy jednoczesnie ilosc sniegu ktora sie roztopila i kiedy S[i]-days<=0 zwracamy wartosc counter
# zlozonosc mniejsza niz O(nlogn)


def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapyfiy(arr,n,i):
    l=left(i)
    r=right(i)

    max_ind=i

    if l<n and arr[l]>arr[max_ind]:
        max_ind=l
    if r<n and arr[r]>arr[max_ind]:
        max_ind=r

    
    if max_ind!=i:
        arr[i],arr[max_ind]=arr[max_ind],arr[i]
        heapyfiy(arr,n,max_ind)


def build_heap(arr):
    n=len(arr)
    for i in range(parent(n-1),-1,-1):
        heapyfiy(arr,n,i)




def heap_sort(arr,max_val):
    stop=0
    n=len(arr)
    if max_val<n:
        stop=n-max_val-1

    build_heap(arr)
    for i in range(n-1,stop,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapyfiy(arr,i,0)



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

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
