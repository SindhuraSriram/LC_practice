class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        isVowel = lambda x: x in 'aeiou'

        sm = mx = sum(map(isVowel, s[:k]))

        for i in range(len(s) - k):
            sm+= isVowel(s[i+k]) - isVowel(s[i])
            mx = max(sm, mx)
        return mx

       