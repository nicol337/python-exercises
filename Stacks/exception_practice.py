
import math

while True:

		num = input("Please enter a number")
		if (int(num) < 0):

			raise RuntimeError("Don't use a negative...please")
		else:
			print(abs(math.root(int(num))))

	