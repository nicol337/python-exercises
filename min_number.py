def n2FindMin(array):
	if array:
		min_num=array[0]
		for num in array:
			isMin = True
			for num2 in array:
				if num > num2:
					isMin = False
			if isMin:
				min_num = num
		return min_num 

def nFindMin(array):
	if array:
		min_num=array[0]
		for num in array:
			if num < min_num:
				min_num = num
		return min_num

def main():
	array = [9,8,9,7,6,0,4,5,-1,-3,-10,10,-3]
	min_of_array = nFindMin(array)
	if min_of_array:
		print(min_of_array)
	min_of_array2 = n2FindMin([1,2,3,4,5,6,7,-10,10,98,-8,-100])
	if min_of_array2:
		print(min_of_array2)


if __name__ == "__main__":
	main()
