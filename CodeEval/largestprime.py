N = 1000

def isPrime(num):
    #all primes are of the form 6k+i greater than 2 and 3
    if num <= 1:
        return False
    #checks 2 and 3
    elif num == 2 or num == 3:
        return True
    #checks 6k+0, 6k+2, 6k+4, 6k+3
    elif num%2 == 0 or num%3 == 0:
        return False
    #checks 6k+5 = 6k - 1 and 6k + 1
    else:
        i = 5
        while i*i <= num:
            if num%i == 0 or num%(i+2) == 0:
                return False
            i = i + 6
        return True
    

def isPalindrome(num):
    return str(num) == str(num)[::-1]
    
for i in range(N-1,0,-1):
    if isPalindrome(i) and isPrime(i):
        print(i)
        break
