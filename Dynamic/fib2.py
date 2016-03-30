
def forLoopFib(n):
	fibNums = [0,1]
	for num in range(2,n+1):
		fibNums.append(fibNums[num-1]+fibNums[num-2])
	return fibNums[n]

# for i in range(10):
# 	print(forLoopFib(i))

def tupleFib(a,b):
	''' '''
	if a == 0 and b == 1:
		return 1
	return tupleFib(a-1,b-2)
