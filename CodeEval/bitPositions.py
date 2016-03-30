
import sys

def dec2bin(num):
    valStr = ''
    stack = []
    while num > 0:
        remainder = num % 2
        stack.append(remainder)
        num = num//2
    while stack:
        valStr = valStr + str(stack.pop())
    print(valStr)
    return valStr
    
    

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num,p1,p2 = map(int,test.split(','))
        binStr = dec2bin(num)
        if binStr[p1-1] == binStr[p2-1]:
            print('true')
        else:
            print('false')
        
