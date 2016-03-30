import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words,pos = test.split(';')
    words,pos = words.split(), [int(x) for x in pos.split()]
    missingPos = set(range(1,len(words)+1)).difference(set(pos))
    for p in missingPos:
        pos.append(p)
    realString = ''
    posNwords = list(zip(pos,words))
    posNwords.sort()
    for p,w in posNwords:
        print(w)
    
    
test_cases.close()
