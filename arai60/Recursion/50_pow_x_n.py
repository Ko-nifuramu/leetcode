"""
step1
approach1: 無難にfor文でnまたは-n回回していく解放

"""



#time: O(N)
#space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            x = 1/x
            n = -n
        for _ in range(n):
            ans *= x
        return ans


#time: O(lonN)
#sapce: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        
        if n%2 == 0:
            return self.myPow(x**2, n//2)
        else:
            return self.myPow(x**2, n//2) * x
        

#iterativeで作成、個人的に発想としては
# 直感的ではあるが、追うのは難しそう
#time: O(lonN)
#space: O(1)
class Solution:

    """
    x = 2, n = 13
    x = 2^13 = 4^6 * 2 = 8^3 * 2 = 64^2 * 8 * 2
    """
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        powered_num = 1
        while n >0 :
            if n % 2 == 1:
                powered_num *= x
            x *= x
            n  = n//2
        
        return powered_num

# 4th-2
# left to right binary exponentationを書き直し。
# ```
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        # left to right binary exponentation
        # exponeitationを2進数表記して2進数表記の各桁ごとに分解する
        # 例) 3^14 = 3^(2^3) * 3^(2^2) * 3^(2^1)
        cumprod = 1
        powered = x
        while n > 0:
            if n % 2:
                cumprod *= powered
            powered *= powered
            n >>= 1
        return cumprod