def atoi(numstr,base):
	num = 0
	exp = 0
	for i in range(len(numstr)-1, -1, -1):
		num+=int(numstr[i])*(base**exp)
		exp+=1
	return num

def revString(word):
	temp = ''
	word = list(word)
	for i in range(len(word)//2):
		temp = word[i]
		word[i]=word[len(word)-1-i]
		word[len(word)-1-i] = temp
	return ''.join(word)

print(atoi('111',10))
print(atoi('111',2))
print(atoi('111',8))

print(revString('abcdefg'))
print(revString('abcdef'))
