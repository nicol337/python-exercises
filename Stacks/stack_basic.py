from stack import Stack

def revString(mystr):
	stck = Stack()
	for letter in mystr:
		stck.push(letter)
	while not stck.isEmpty():
		print(stck.pop())

def symmetricString(mystr):
	stck = Stack()
	i = 0
	while i < len(mystr):
		if mystr[i] == '(':
			stck.push(mystr[i])
		elif mystr[i] == ')':
			if stck.isEmpty():
				return False
			else:
				stck.pop()
		i+=1
	if stck.isEmpty():
		return True
	return False

def dec2Bin(num):
	stck = Stack()
	binary = ''
	while num > 0:
		remainder = num%2
		stck.push(remainder)
		num = num // 2
	while not stck.isEmpty():
		binary += str(stck.pop())
	return binary

def dec2Hex(num):
	stck = Stack()
	hex_str = ''
	hex_vals = ''.join([str(i) for i in range(10)]) + ''.join([chr(i) for i in range(65,71)])
	while num > 0:
		remainder = num % 16
		stck.push(remainder)
		num = num // 16

	while not stck.isEmpty():
		hex_str += hex_vals[stck.pop()]
	return hex_str
	# while not stck.isEmpty():

def dec2Oct(num):
	stck = Stack()
	oct_str = ''
	while num > 0:
		remainder = num%8
		stck.push(remainder)
		num = num // 8
	while not stck.isEmpty():
		oct_str += str(stck.pop())
	return oct_str

def genConverter(num, base):
	stck = Stack()
	val_str = ''
	while num > 0:
		remainder = num % base
		stck.push(remainder)
		num = num // base
	while not stck.isEmpty():
		val_str += str(stck.pop())
	return val_str


def main():
	stck = Stack()
	for letter in "hello":
		stck.push(letter)

	print(stck.size())
	print(stck.peek())
	print(stck.peek())
	while not stck.isEmpty():
		print(stck.pop()) 
	print(symmetricString("(( ) ( ) ( ) ) "))

	revString("nicolelee")
	print(dec2Bin(9))
	print(dec2Hex(256))
	print(dec2Oct(25))
	print(genConverter(26,26))
	# for i in range(101):
		# print(divBy2(i))
	# print(', '.join([str(i) for i in range(10)]))




main()