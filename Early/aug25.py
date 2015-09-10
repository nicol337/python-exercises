class Car:
	def __init__(self,model):
		self.model = model

	def __str__(self):
		return str(self.model)

def main():
	car1 = Car("Mazda3")
	print(car1)
	


if __name__ == "__main__":
	main()