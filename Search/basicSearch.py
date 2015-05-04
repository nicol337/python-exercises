import random

def unsortedSeqSearch(array, key):
	pos = -1

	for index in range(len(array)):
		if array[index] == key:
			pos = index
			return pos
	return -1

def sortedSeqSearch(array, key):
	pos = -1

	for index in range(len(array)):
		if array[index] == key:
			pos = index
			return pos
		elif array[index] > key:
			return -1
	return -1
	
def binarySearch(array, key):
	middle = len(array)//2
	if not array:
		return -1
	
	elif array[middle]==key:
		return middle
	elif array[middle] > key:
		print('left',array[middle])
		return binarySearch(array[:middle],key)
	else:
		print('right',array[middle])
		index = binarySearch(array[middle+1:],key)
		return index+middle+1 if index != -1 else index

def create_array():
	itr = -100
	array = []
	index = random.randint(1,99)
	for i in range(100):
		if i == index:
			itr = index
			array.append(itr)
			itr+=2
		else:
			array.append(itr)
			itr+=1
	print (index)	
	return array, index

def main():
	# print(unsorted([1,2,3,4,5,6],8))
	array,index = create_array()
	print(array)
	print('binarySearch')
	print(binarySearch(array,index))


if __name__ == "__main__":
	main()





