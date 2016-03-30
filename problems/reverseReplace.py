'''
reverse a sentence and replace the origWord with repWord in all cases.
? Are there only spaces and alphanumeric characters?
? How long is this sentence?

'''

def reverseAndReplace(sent,orig,rep):
	toks = sent.split()
	for i in range(len(toks)//2):
		if toks[i] == orig:
			toks[i] = rep
		if toks[-i-1] == orig:
			toks[-i-1] = rep
		toks[i],toks[-i-1] = toks[-i-1],toks[i]
	return " ".join(toks)

def lazyReverseAndReplace(sent,orig,rep):
	return " ".join(sent.replace(origWord,repWord).split()[::-1]))

def main():
	sent = 'I like cats cats dogs sheep pig no way'
	origWord = 'cats'
	repWord = 'dogs'
	print(lazyReverseAndReplace(sent,origWord,repWord))

	print(reverseAndReplace(sent,origWord,repWord))

main()