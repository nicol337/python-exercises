class Car:
	def __str__(self):
		return "I'm just a car"
	def speed(self):
		print("I'm at speed 10")
	
class Toyota(Car):
	def __str__(self):
		return "I'm not just a car, I'm a Toyota"

def main():
	car = Car()
	toyota = Toyota()
	print(car)
	print(toyota)
	car.speed()
	toyota.speed()

if __name__ == "__main__":
	main()
