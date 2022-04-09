# This is yet to be filled
def SelectionSort(arr):
    for i in range(0,len(arr)):
        index = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[index]:
                index = j
        arr[i],arr[index] = arr[index],arr[i]
        print("The Array after Pass {} is {}".format(i+1,arr))
    print("\nThe Final Sorted Array: {}".format(arr))
