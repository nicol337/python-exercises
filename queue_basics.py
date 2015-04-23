from queue import Queue
from deque import Deque


def test():
	dq = Deque()

	for i in range(65,70):
		dq.addFront(chr(i))
		dq.addRear(chr(i).lower())
		print(dq.size())

	while not dq.isEmpty():
		
		print(dq.removeFront())
		print(dq.removeRear())
		print(dq.items)

def isPalindrome(word, case_sensitive=True):
	"""Return True/False if palindrome"""
	dq = Deque()
	word = word if case_sensitive else word.lower()
	for letter in word:
		dq.addRear(letter)

	for i in range(len(word)//2):
		if dq.removeRear() != dq.removeFront():
			return False

	return True

def main():
	print(isPalindrome("ABAba"))
	print(isPalindrome("ABAba", False))
	print(isPalindrome("abba"))

main()

