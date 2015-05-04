def bubbleSort(alist):
	exchanges = True
	passnum = len(alist)-1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		passnum = passnum-1
	return alist


def selectionSort(alist):
	end = len(alist)-1
	for i in range(len(alist)):
		nextMax = 0
		for j in range(1,end+1):
			if alist[nextMax] < alist[j]:
				nextMax = j
		
		print(alist[nextMax], alist[end])
		temp = alist[end]
		alist[end] = alist[nextMax]
		alist[nextMax] = temp
		end-=1
		print(alist)

def mergeSort(alist):
	print(alist)
	if len(alist)>1:
		mid = len(alist)//2
		left = alist[:mid]
		right = alist[mid:]
		mergeSort(left)
		mergeSort(right)
		l=0
		r=0
		for k in range(len(alist)):
			print('in merge', left, right,alist)
			if r >= len(right):
				alist[k]=left[l]
				l+=1
			elif l >= len(left):
				alist[k]=right[r]
				r+=1
			else:
				if right[r] > left[l]:
					alist[k] = left[l]
					l+=1
				else:
					alist[k] = right[r]
					r+=1

def mergeSort2(array):
	
	if len(array)>=2:
		mid =len(array)//2
		left = array[:mid]
		right = array[mid:]
		left_index= 0
		right_index= 0
		mergeSort(left)
		mergeSort(right)
		
		for index in range(len(array)):
			if left_index >= len(left):
				array[index] = right[right_index]
				right_index += 1
			elif right_index >= len(right):
				array[index] = left[left_index]
				left_index +=1
			else:
				if left[left_index] < right[right_index]:
					array[index] = left[left_index]
					left_index += 1
				else:
					array[index] = right[right_index]
					right_index +=1

def mergeSort3(alist):
	
	if len(alist) > 1:
		mid = len(alist)//2
		left = alist[:mid]
		right = alist[mid:]
		left_index = 0
		right_index = 0
		mergeSort(left)
		mergeSort(right)
		for k in range(len(alist)):
			if left_index >= len(left):
				alist[k] = right[right_index]
				right_index +=1
			elif right_index >= len(right):
				alist[k] = left[left_index]
				left_index += 1
			else:
				if right[right_index] > left[left_index]:
					alist[k] = right[right_index]
					right_index += 1
				else:
					alist[k] = left{left_index]
					left_index += 1


# print(bubbleSort([4,3,2,1,0,9]))
# print(selectionSort([4,3,2,1,0,9]))
alist = [93,45,6,7,1,2,34,76,34,-19,23,102,3042,545,90293,10,19992,394928,12,3,4,2,3]
mergeSort2(alist)
print(alist)