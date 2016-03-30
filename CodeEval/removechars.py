

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    sentence,char2remove = test.split(',')
    charList = list(sentence.replace(' ',','))
    for c in char2remove:
        while c in charList:
            charList.remove(c)
    print(''.join(charList).replace(',',' '))
    

test_cases.close()
