class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = max(candies)
        ans = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= l:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        