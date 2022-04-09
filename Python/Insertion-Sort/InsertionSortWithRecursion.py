# Insertion Sort With Recursion
def InsertSortWithRecusion(arr,n):
    if n<=1:
        return
    
    InsertSortWithRecusion(arr,n-1)
    print("After Pass {} Array is = {}".format((n-1),arr))

    last = arr[n-1]
    j = n-2
    while j>=0 and last<arr[j]:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = last
