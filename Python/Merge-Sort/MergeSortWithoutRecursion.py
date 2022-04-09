# Merge two sorted sublists `A[frm…mid]` and `A[mid+1…to]`
def merge(A, temp, frm, mid, to):
 
    k = frm
    i = frm
    j = mid + 1
 
    # loop till no elements are left in the left and right runs
    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i = i + 1
        else:
            temp[k] = A[j]
            j = j + 1
 
        k = k + 1
 
    # copy remaining elements
    while i < len(A) and i <= mid:
        temp[k] = A[i]
        k = k + 1
        i = i + 1
 
    # copy back to the original list to reflect sorted order
    for i in range(frm, to + 1):
        A[i] = temp[i]
 
 
# Iteratively sort sublist `A[low…high]` using a temporary list
def MergeSortWithoutRecursion(A):
 
    low = 0
    high = len(A) - 1
 
    temp = A.copy()

    count=1
    m = 1
    while m <= high - low:
        for i in range(low, high, 2*m):
            frm = i
            mid = i + m - 1
            to = min(i + 2*m - 1, high)
            merge(A, temp, frm, mid, to)
        
        print("Array after pass {} is {}".format(count,A))
        count+=1
        m = 2*m
    print("\nThe final sorted array = {}".format(A))
