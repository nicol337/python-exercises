import sys
test_cases = open(sys.argv[1], 'r')

def dec2bin(num):
    binStr = ''
    stack = []
    while num > 0:
        remainder = num % 2
        stack.append(remainder)
        num = num // 2
    while stack:
        binStr = binStr + str(stack.pop())
    return binStr
    
def count1s(binStr):
    numArray = [int(dig) for dig in binStr]
    return sum(numArray)

for test in test_cases:
    binStr = dec2bin(int(test))
    oneCnt = count1s(binStr)
    print(oneCnt)

test_cases.close()