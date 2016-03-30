import sys
test_cases = open(sys.argv[1], 'r')

def isPalindrome(num):
    string = str(num)
    return string == string[::-1]

for test in test_cases:
    num = int(test)
    ctr = 0
    while not isPalindrome(num):
        num += int(str(num)[::-1])
        ctr += 1
    
    print(ctr,num)

test_cases.close()
