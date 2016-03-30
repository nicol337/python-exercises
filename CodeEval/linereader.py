import sys
test_cases = open(sys.argv[1],'r')
N = test_cases.readline()
for test in test_cases:
	print(test)
print(N)
test_cases.close()
