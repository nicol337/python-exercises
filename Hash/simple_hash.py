from hashTable import HashTable


H=HashTable()

def printStuff():
	for a,z in zip(H.slots, H.data):
		print(a,z)
	print('\n')


H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

printStuff()

H[20]="puppies!"

printStuff()


