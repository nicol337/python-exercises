def mergeSort(array, tmpArray, left, right):
   
    middle = (right - left)//2 + left
    if left < middle:
        mergeSort(array, tmpArray, left, middle)
        mergeSort(array, tmpArray, middle+1, right)

        leftPtr, rightPtr, arrayPtr = left, middle+1, left
        t
        while leftPtr <= middle and rightPtr <= right:
            if array[rightPtr] < array[leftPtr]:
                tmpArray[arrayPtr] = array[arrayPtr]
                array[arrayPtr] = array[rightPtr]
                rightPtr += 1
            else:
                rightPtr += 1
            arrayPtr += 1
        while leftPtr <= middle:

        while rightPtr <= right:


        


array = [9,8,7,6,5,4,3,2,1]
tmpArray = [0 for i in array]
mergeSort(array,0,len(array)-1)
print(array)


