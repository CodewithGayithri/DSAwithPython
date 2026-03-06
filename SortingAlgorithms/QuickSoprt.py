def partition(arr, low, high):
    pivot = arr[low]
    i=low 
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j >=low+1:
            j -= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = list(map(int,input("enter The Array: ").split()))

def quicksort(arr,low,high):
    if low<high:
        p_indx = partition(arr,low,high)
        quicksort(arr,low,p_indx-1)
        quicksort(arr,p_indx+1, high)

quicksort(arr,0,len(arr)-1)
print("sorted array: ",arr)

