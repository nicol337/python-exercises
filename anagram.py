def anagram(s1, s2):
	dict1 = {}
	dict2 = {}

	for letter in s1:
		if letter not in dict1:
			dict1[letter] = 0
		dict1[letter]+=1
	for letter in s2:
		if letter not in dict2:
			dict2[letter] = 0
		dict2[letter]+=1
	return dict1==dict2

def anagram2(s1, s2):
	s1 = list(s1.lower()).sort()
	s2 = list(s2.lower()).sort()

	return s1 == s2

def anagram3(s1,s2):
	indices_found_s2 = []

	for index1 in range(len(s1)):
		found = False
		for index2 in range(len(s2)):
			if s1[index1] == s2[index2] and index2 not in indices_found_s2:
				indices_found_s2.append(index2)
				found = True
				break
		if not found:
			return False
	return True

	
def main():
	print(anagram("abbcdef","feddcab"))
	print(anagram2("asdfghjkl","lkjasdfgh"))
	print(anagram3("aaaaabbb","aaaabbbb"))


if __name__ == "__main__":
	main()

