def getPermutations(word):
	if len(word) <= 1:
		return [word]
	combos = []
	for i in range(len(word)):
		permutations = getPermutations(word[:i]+word[i+1:])
		for permutation in permutations:
			combos.append(word[i]+permutation)
	return combos

global ctr
ctr = 0

def getDistinctPermutations(word):
	global ctr

	if len(word) <= 1:
		ctr += 1
		return [word]

	combos = set()
	for i in range(len(word)):
		permutations = getDistinctPermutations(word[:i]+word[i+1:])
		for permutation in permutations:
			combos.add(word[i]+permutation)
			
	return combos

print(getPermutations("abcde"))
print(getDistinctPermutations("abcde"))
print(ctr)