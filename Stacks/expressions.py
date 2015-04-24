from stack import Stack

def inorderInfix(expression):
	num_stck = Stack()
	op_stck = Stack()
	itr = 0
	while itr < len(expression):
		char = expression[itr]
		if char == ')':
			val1 = num_stck.pop()
			val2 = num_stck.pop()
			op = op_stck.pop()
			total = calc(val1,val2,op)
			num_stck.push(total)
		elif char.isdigit():
			num_stck.push(char)
		elif char in ['*','-','/','+']:
			op_stck.push(char)
		itr += 1

	return num_stck.pop()

def calc(val1, val2, op):
	if op == '*':
		return float(val1) * float(val2)
	elif op == '+':
		return float(val1) + float(val2)
	elif op == '-':
		return float(val1) - float(val2)
	elif op == '/':
		return float(val1) / float(val2)
	else:
		print("Invalid operand")


def main():
	print(inorderInfix(''))


if __name__ == '__main__':
	main()