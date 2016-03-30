

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    toks = [int(x) for x in test.split()]
    div1,div2,upto = toks[0],toks[1],toks[2]
    for num in range(1,upto+1):
        if num%div1 ==0 and num%div2 == 0:
            print('FB',end='')
        elif num%div1 == 0:
        	print('F',end='')
        elif num%div2 == 0:
        	print('B',end='')
        else:
        	print(num,end='')
        if num < upto:
        	print(' ',end='')
        else:
        	print('\n')

test_cases.close()