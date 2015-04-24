class Fraction:
	def __init__(self,top,bottom):
		self.num = top
		self.den = bottom
		self.simplify()

	def simplify(self):
		for i in range(min(abs(self.num), abs(self.den)),0,-1):
			if self.num % i == 0 and self.den % i == 0:
				self.num /= i
				self.den /= i
		self.num = int(self.num)
		self.den = int(self.den)

	def __add__(self,other):
		new_den = self.den * other.den
		new_num = (self.num * other.den) + (other.num * self.den)
		

		return Fraction(new_num,new_den)

	def __eq__(self,other):
		return self.num == other.num and self.den == other.den

	def __str__(self):
		display_num = 0
		display_den = self.den
		display_whole = 0

		display_str = ""
		if self.num == 0:
			display_str = int(display_whole)
		elif abs(self.num) >= self.den:
			display_whole = self.num // self.den
			display_num = self.num % self.den
			if display_num == 0:
				display_str = int(display_whole)
			else:	
				display_num = int(display_num)
				display_den = int(display_den)
				display_whole = int(display_whole)
				display_str = str(display_whole) + " "+ str(display_num) + "/" + str(display_den)
		else:
			display_num = int(self.num)
			display_den = int(self.den)	
			display_str = str(display_num)+"/"+str(display_den)

		return str(display_str)

def gcd(num1,num2):
	while num1%num2 != 0:
		old_num1 = num1
		old_num2 = num2
		num1 = old_num2
		num2 = old_num1%old_num2
	

def main():
	while True:
		frac1 = input("Please enter first fraction").split("/")
		frac2 = input("Please enter first fraction").split("/")
		frac1 = [int(x) for x in frac1]
		frac2 = [int(x) for x in frac2]

		frac1 = Fraction(frac1[0],frac1[1])
		frac2 = Fraction(frac2[0],frac2[1])

		print("frac1 == frac2:",frac1 == frac2)
		print(frac1,"+",frac2,"=",frac1+frac2)

if __name__ == "__main__":
	main()

