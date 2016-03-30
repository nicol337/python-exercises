

import sys
test_cases = open(sys.argv[1], 'r')
    

for test in test_cases:
    if test:
        nums, total = test.split(';')
        total = int(total)
        nums = [int(x) for x in nums.split(',')] #maybe duplicates in list? consider
        pairs = list()
        for index in range(len(nums)):
            if total-nums[index] in nums[index+1:]:
                pairs.append(str(nums[index])+','+str(total-nums[index]))

        


        if pairs:
            print(';'.join(pairs))
        else:
            print('NULL')
        

test_cases.close()
