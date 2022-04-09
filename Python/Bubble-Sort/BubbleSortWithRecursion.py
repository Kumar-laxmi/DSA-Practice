def bubbleSortRecursive(array, n=None): #Recursive
        if n is None:
            n = len(array)
 
        # Base case
        if n == 1:
            return
 
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        
        print("The Array after Pass is {}".format(array))
        bubbleSortRecursive(array, n-1)
