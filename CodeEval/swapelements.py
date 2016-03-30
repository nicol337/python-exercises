import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums,swaps = test.split(':')
    nums = nums.split()
    swaps = swaps.split(',')
    for pair in swaps:
        a,b=pair.split('-')
        a,b = int(a),int(b)
        nums[a],nums[b] = nums[b],nums[a]
    print(' '.join(nums))
    

test_cases.close()
