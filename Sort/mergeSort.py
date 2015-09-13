def mergeSort2(array):
    if len(array) > 1:
        
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort2(left)
        mergeSort2(right)

        leftPtr,rightPtr,arrayPtr = 0,0,0
        while leftPtr < len(left) and rightPtr < len(right):
            if right[rightPtr] < left[leftPtr]:
                array[arrayPtr] = right[rightPtr]
                rightPtr += 1
            else:
                array[arrayPtr] = left[leftPtr]
                leftPtr += 1
            arrayPtr += 1
        while leftPtr < len(left):
            array[arrayPtr] = left[leftPtr]
            leftPtr += 1
            arrayPtr += 1
        while rightPtr < len(right):
            array[arrayPtr] = right[rightPtr]
            rightPtr += 1
            arrayPtr += 1
        

array = [9,8,7,6,5,4,3,2,1]
print(mergeSort2(array),array)










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
            pass
        while rightPtr <= right:
            pass

        







