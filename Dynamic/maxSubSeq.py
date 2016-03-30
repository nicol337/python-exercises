

def maxSubSeq(array, j, maxSumSoFar):
	if j <= 0 :
		return maxSumSoFar
	possibleNewMax = max(maxSubSeq(array,j-1,maxSumSoFar)+array[j],array[j])
	print(j,possibleNewMax,maxSumSoFar)
	maxSumSoFar = max(possibleNewMax,maxSumSoFar)
	print(j,possibleNewMax,maxSumSoFar)
	return maxSumSoFar


array = [-9,-8,-7,1,2,-3,3,4,-10]
print(maxSubSeq(array, len(array)-1, array[-1]))