import random

def bs(array, left_index, right_index):
	print("(",left_index,right_index,")")
	mid_index = ((right_index - left_index) // 2)+left_index
	if array[mid_index] == mid_index:
		return mid_index
	elif left_index == right_index:
		return -1
	elif array[mid_index] > mid_index:
		return bs(array,left_index, mid_index)
	else:
		return bs(array,mid_index,right_index)	

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
	return array

def main():
	array = create_array()
	print(array)
	print(bs(array,0,len(array)))


if __name__ == "__main__":
	main()
