class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
                # Initialize leftSum & rightSum to store the sum of all the numbers strictly to the index's left & right respectively...
        leftSum, rightSum = 0, sum(nums)
        # Traverse elements through the loop...
        for idx, ele in enumerate(nums):
            rightSum -= ele
            # If the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right...
            if leftSum == rightSum:
                return idx      # Return the pivot index...
            leftSum += ele
        return -1

        