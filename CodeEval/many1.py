#10 -> 1000
import sys
test_cases = open(sys.argv[1],'r')
for test in test_cases:
	num = int(test)
	binary = ''
	while num != 0:
		if num%2 == 0:
			binary += '1'
		else:
			binary += '0'
		num = num//2
