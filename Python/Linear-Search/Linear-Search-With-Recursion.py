def LinearSearchRecursive(arr,key,index=0):
    if index>=len(arr):
        return -1
    elif arr[index]==key:
        return index+1
    else:
        return LinearSearchRecursive(arr,key,index+1)

arr = list(int(num) for num in input("Enter the array: ").strip().split())
key = int(input("Enter the key value to search: "))

print("The array is = {}".format(arr))
print("The key element is = {}".format(key))

pos = LinearSearchRecursive(arr,key)
if pos==-1:
    print("\nSorry! Key element = {} not present in Array = {}".format(key,arr))
else:
    print("\nThe key element = {} found at position = {}".format(key,pos))
