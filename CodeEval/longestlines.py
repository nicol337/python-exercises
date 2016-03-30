import sys
test_cases = open(sys.argv[1], 'r')
N = int(test_cases.readline())
wordsNLens = {}
for test in test_cases:
    wordsNLens[len(test)] = test
for length in sorted(wordsNLens.keys(),reverse=True)[:N]:

    print(wordsNLens[length])
test_cases.close()
