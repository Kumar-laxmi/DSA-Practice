def BinarySeachRecursive(arr,x,low=0,high=len(arr)-1):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid+1
        elif arr[mid] > x:
            return BinarySeachRecursive(arr, x, low, mid - 1)
        else:
            return BinarySeachRecursive(arr, x, mid + 1, high)
    else:
        return -1

arr = list(int(num) for num in input("Enter the array: ").strip().split())
key = int(input("Enter the key value to search: "))

print("The array is = {}".format(arr))
print("The key element is = {}".format(key))

pos = BinarySeachRecursive(arr,key)
if pos==-1:
    print("\nSorry! Key element = {} not present in Array = {}".format(key,arr))
else:
    print("\nThe key element = {} found at position = {}".format(key,pos))
