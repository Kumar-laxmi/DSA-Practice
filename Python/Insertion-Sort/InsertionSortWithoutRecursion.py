# Insertion Sort Without Recursion
def InsertSortWithoutRecusion(arr):
    n = len(arr)
    
    for i in range(1,n):
        print("The Array in Pass {} is {}".format(i,arr))
        key = arr[i]
        j = i - 1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    
    print("\nThe Final Sorted Array = {}".format(arr))
