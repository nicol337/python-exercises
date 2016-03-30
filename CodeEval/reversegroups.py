import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numbers,delta = test.split(';')
    numbers = numbers.split(',')
    delta = int(delta)
    old_delta = delta
    if 1 < delta <= len(numbers):
	    numbers = numbers[:delta][::-1]+numbers[delta:]
	    for i in range(delta,len(numbers),delta):
	        numbers = numbers[:old_delta]+numbers[old_delta:i][::-1]+numbers[i:]
	        old_delta = delta
    print(','.join(numbers))

test_cases.close()