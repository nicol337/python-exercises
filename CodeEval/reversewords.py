import sys
test_cases = open(sys.argv[1], 'r')
for case in test_cases:
	if case:
		words = case.split()
		words = words[::-1]
		print(" ".join(words))
test_cases.close()