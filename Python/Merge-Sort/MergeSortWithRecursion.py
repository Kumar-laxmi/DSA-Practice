def MergeSortWithRecursion(arr,i=1):
    if len(arr) < 2:
        return arr
 
    middle = int(len(arr)/2)
    print("After pass {} Left array is: {}".format(i,arr))
    left = MergeSortWithRecursion(arr[:middle],i+1)
    print("After pass {} Right array is: {}".format(i,arr))
    right = MergeSortWithRecursion(arr[middle:],i+1)
 
    return Merge(left, right)

def Merge(Left,Right):
    if Left==[] and Right==[]:
        return []
    elif Left!=[] and Right==[]:
        return Left
    elif Left==[] and Right!=[]:
        return Right
    
    if Left[0]<Right[0]:
        return [Left[0]] + Merge(Left[1:],Right)
    else:
        return [Right[0]] + Merge(Left,Right[1:])
