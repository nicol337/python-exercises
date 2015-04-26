def sumList(numbers):
	if not numbers:
		return 0
	elif len(numbers) == 1:
		return numbers[0]
	else:
		return sumList(numbers[1:])+numbers[0]

def factorial(num):
	if num <= 1:
		return 1
	else:
		return factorial(num-1) * num


def main():

	print(sumList([1,2,3,4,5,6,7,8,9,10]))
	print(factorial(9))

main()