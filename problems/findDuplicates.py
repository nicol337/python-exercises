'''
find duplicates in a list in O(n) time and O(1) space

traverse the list for i= 0 to n-1 elements
{
  check for sign of A[abs(A[i])] ;
  if positive then
     make it negative by   A[abs(A[i])]=-A[abs(A[i])];
  else  // i.e., A[abs(A[i])] is negative
     this   element (ith element of list) is a repetition
}

'''
def printDuplicates(array):
	for i in range(len(array)):
		if array[abs(array[i])] > 0:
			array[abs(array[i])] *= -1
		else:
			print(abs(array[i]),' ',end='')
	print(array)
	

'''
Find the one digit in an array that's not repeated
If so, we could start with a variable unique_delivery_id set to 00 and run some bitwise operation with that variable and each number in our list. If duplicate integers cancel each other out, then we’d only be left with the unique integer at the end!

Which bitwise operation would let us do that?

Solution
We XOR ↴ all the integers in the list. We start with a variable unique_delivery_id set to 00. Every time we XOR with a new ID, it will change the bits. When we XOR with the same ID again, it will cancel out the earlier change.

In the end, we'll be left with the ID that appeared once!
'''
def printUniques(array):
    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    print unique_delivery_id
   

def main():
	array = [1,2,3,2,1]
	printDuplicates(array)
	printUniques(array)

main()

