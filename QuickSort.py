arr=[]
for v in range(7):
    arr.append(int(input("Enter a number: ")))
print(arr)

def partition(arr, low, high ):
    pivot=arr[high]
    i=low-1
    for j in range (low, high):
        if arr[j] <=pivot:
            i = i+1
            arr[i], arr[j]= arr[j],arr[i]
    arr[i+1], arr[high]=arr[high], arr[i+1]        
    return i+1        
        
        
def quicksort(arr, low, high):
    if low < high:
        q=partition(arr, low, high)
        quicksort(arr, low, high-1)
        quicksort(arr,q+1, high)

        
quicksort(arr, 0, len(arr)-1)
for u in range(len(arr)):
    print(arr[u])
    
    

    

       
        
        
