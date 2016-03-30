import random


def shuffle(array):
	for i in range(len(array)):
		j = random.randint(i,len(array)-1)
		array[i], array[j] = array[j],array[i]
	
	return array

def testDistribution(array):
	counts = [[0 for x in range(len(array))] for x in range(len(array))]
	for i in range(100000):
		shuffle(array)
		for i in range(len(array)):
			counts[i][array.index(i)] += 1
	print (counts)



def main():
	array = [0,1,2,3,4,5,6,7,8,9]
	print(shuffle(array))
	testDistribution(array)

main()