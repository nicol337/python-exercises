def insert(word, trie):
	currNode = trie
	for letter in word:
		if letter not in currNode:
			currNode[letter] = {}
		currNode = currNode[letter]
	currNode[None] = None

def find(word, trie):
	currNode = trie
	for letter in word:
		print(letter)
		if letter in word:
			currNode = currNode[letter]
		else:
			return False
	if None in currNode:
		return True
	return False

def preOrder(trie, subword):
	if None in trie:
		return [subword]
	allWords = []
	for letter in trie:
		words = preOrder(trie[letter],subword+str(letter))
		allWords += words
	return allWords


trie = {}
insert("halo",trie)
insert("hallo",trie)
insert("shoe",trie)
insert("shone",trie)
insert("shine",trie)
print(trie)
print(find("shin",trie))
print(preOrder(trie,""))