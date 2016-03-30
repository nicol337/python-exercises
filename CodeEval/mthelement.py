# a b c d 4
import sys
test_cases = open(sys.argv[1],'r')
for test in test_cases:
	toks = test.split()
	chars = toks[:-1]
	m = int(toks[-1])
	if m <= len(chars):
		print(toks[len(toks)-m-1])


