class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        isVowel = lambda x: x in 'aeiou'           # <-- 1)

        sm = mx = sum(map(isVowel, s[:k]))          # <-- 2)

        for i in range(len(s) - k):                 # 
            sm+= isVowel(s[i+k]) - isVowel(s[i])    # <-- 3)
            if sm > mx: mx = sm                     #

        return mx
        