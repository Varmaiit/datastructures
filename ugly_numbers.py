# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
import math, cmath


class Solution:
    def isUgly(self, n:int) -> bool:
        _allowed = [1,2,3,5]
        if n in _allowed:
            return True
        # approach trying to find all prime factors of n
        # do a check if that prime factor is not in 2, 3, 5 return True 
        try:
            b = math.sqrt(n)
        except:
            b = cmath.sqrt(n).imag
        for i in range(3, int(b) + 1, 2):
            while n % i == 0:
                if n not in _allowed:
                    return False
                n = n / i
            if n not in _allowed:
                return False
        return True
                
    def primeFactors(self, n):
        """
        prime factors of n
        """
        c = 2
        while(n > 1):
            print("n", n, c)
    
            if(n % c == 0):
                print(c, end=" ")
                n = n / c
                print("n in f", n)
            else:
                c = c + 1

    
if __name__ == "__main__":
    sol = Solution()
    n = 315
    ans = sol.isUgly(-2147483648)
    print("answer", ans)

