import sys
test_cases = open(sys.argv[1],'r')

def decTo26base(num):
	stack = []
	val_str = ''
	letters = ' '+''.join([chr(i) for i in range(65,91)])
	while num > 0:
		remainder = num % 26
		stack.append(remainder)
		num = (num-1)// 26 
	while stack:
		num = stack.pop()
		if num == 0:
			num = 26
		val_str = val_str + letters[num]
	return val_str

for test in test_cases:
	print(decTo26base(int(test)))




