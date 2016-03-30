import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    array = []
    rows = test.split('|')
    for row in rows:
        row = [int(val) for val in row.split()]
        array.append(row)
    maxVals = []+array[0]
    print(maxVals)
    for i in range(1,len(array)):
        for j in range(len(array[0])):
            maxVals[j] = max(maxVals[j], array[i][j])
    print(' '.join([str(val) for val in maxVals]))
    
test_cases.close()