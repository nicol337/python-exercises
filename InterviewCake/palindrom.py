def isPermPal(word):
	d = {}
	for c in word:
		if c in d:
			del d[c]
		else:
			d[c] = 1
	print(d)
	if len(d) in range(0,2):
		return True
	return False

print(isPermPal('civil'))
print(isPermPal('ccivil'))
print(isPermPal('vicci'))
print(isPermPal('civic'))
