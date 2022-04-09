def BubbleSort(arr):  # Non-recusive
    flag = 1
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                flag = 0
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("The Array after Pass {} is {}".format(i+1,arr))
        if flag==1:
            break
    print("\nThe Final Sorted Array is: {}".format(arr))
