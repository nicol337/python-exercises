five_str = "*****"
for i in range(1,10):
	if i <= 5:
		print(five_str[:i])
	else:
		print(five_str[i-5:])


stars = "*********"
space = "      "
for i in range(1,10,2):
	if i <= 5:
		print(space[i:] + stars[:i])
	else:
		print(stars[i-5:])
		
