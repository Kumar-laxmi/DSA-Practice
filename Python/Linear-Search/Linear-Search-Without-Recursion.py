def LinearSearchNonRecursive(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i+1
    return -1

arr = list(int(num) for num in input("Enter the array: ").strip().split())
key = int(input("Enter the key value to search: "))

print("The array is = {}".format(arr))
print("The key element is = {}".format(key))

pos = LinearSearchNonRecursive(arr,key)
if pos==-1:
    print("\nSorry! Key element = {} not present in Array = {}".format(key,arr))
else:
    print("\nThe key element = {} found at position = {}".format(key,pos))
