def BinarySeachNonRecursive(arr,key,low=0,high=len(arr)-1):
    while low<=high:
        mid = low + (high - low)//2
        if arr[mid]==key:
            return mid+1
        elif arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
    return -1

arr = list(int(num) for num in input("Enter the array: ").strip().split())
key = int(input("Enter the key value to search: "))

print("The array is = {}".format(arr))
print("The key element is = {}".format(key))

pos = BinarySeachNonRecursive(arr,key)
if pos==-1:
    print("\nSorry! Key element = {} not present in Array = {}".format(key,arr))
else:
    print("\nThe key element = {} found at position = {}".format(key,pos))
