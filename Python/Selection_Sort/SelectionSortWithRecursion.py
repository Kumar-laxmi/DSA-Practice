def minIndex(a, i, j):
    if i == j:
        return i
         
    k = minIndex(a, i + 1, j)
    return (i if a[i] < a[k] else k)

def recurSelectionSort(a, n, index = 0):
    if index == n:
        return -1
         
    k = minIndex(a, index, n-1)

    if k != index:
        a[k], a[index] = a[index], a[k]
    
    print("The Array after Pass is {}".format(a))
    recurSelectionSort(a, n, index + 1)
