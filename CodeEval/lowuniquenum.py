import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = [int(x) for x in test.split()]
    uniqueNums = set()
    repeatNums = set()
    for num in nums:
        if num in uniqueNums:
            uniqueNums.remove(num)
            repeatNums.add(num)
        elif num not in repeatNums:
            uniqueNums.add(num)
    if uniqueNums:
        print(nums.index(sorted(uniqueNums)[0])+1)
    else:
        print(0)
    

test_cases.close()