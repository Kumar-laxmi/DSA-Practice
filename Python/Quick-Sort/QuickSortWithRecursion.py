def QuickSort(arr,left,right):
    if left<right:
        p = Partition(arr,left,right)
        QuickSort(arr,left,p-1)
        QuickSort(arr,p+1,right)

def Partition(arr,left,right):
    pivot = arr[right]
    i = left - 1

    for j in range(left,right):
        if arr[j]<pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    
    print("The Array after Pass {}\tThe partition variable is: {}".format(arr,i+1))
    return (i + 1)
