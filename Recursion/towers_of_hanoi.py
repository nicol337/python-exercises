peg1 = [1,2,3,4,5]
peg2 = [1,2]
peg3 = []


def moveTower(height, source, destination, temp):
	if height >= 1:
		moveTower(height-1, source, temp, destination)
		print("moving disk from {0} to {1}".format(source, destination))
		moveTower(height-1, temp, destination, source)

moveTower(2,'A','B','C')