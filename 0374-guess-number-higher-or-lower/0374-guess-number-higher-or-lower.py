# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n, s=1):
        m = (s + n) // 2
        g = guess(m)
        n -= (n - m + 1)*g*(g-1)//2     
        s += (m - s + 1)*g*(g+1)//2    
        return m if not g else self.guessNumber(n, s)
        