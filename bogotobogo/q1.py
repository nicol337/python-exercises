def f(x):
	nums = {i**3 for i in range(0,x)}
	return nums

for x in f(5):
	print(x)


