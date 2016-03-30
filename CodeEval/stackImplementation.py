
import sys

class Stack(list):
    def __init__(self):
        self = []
    
    def __pop__(self):
        
        return self.pop()
      
    def push(self,item):
        self.append(item)
    
    def isEmpty(self):
        return self == []
    
def main():
    test_cases = open(sys.argv[1], 'r')
    
    
    
    for test in test_cases:
        items = test.split()
        stck = Stack()
        for item in items:
            stck.push(item)
        alt = 1
        result = ''
        while not stck.isEmpty():
            item = stck.pop()
            if alt == 1:
                result += item+' '
            alt *= -1
        print( result[:-1])
    
    test_cases.close()

main()