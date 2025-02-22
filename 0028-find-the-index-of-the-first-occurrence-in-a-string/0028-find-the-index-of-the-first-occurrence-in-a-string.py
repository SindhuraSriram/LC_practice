class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return 0  # Return 0 if needle is an empty string

        # Iterate through the haystack to find the needle
        for i in range(len(haystack) - n + 1):  # Ensure valid slicing
            if haystack[i:i + n] == needle:
                return i  # Return the first index where needle matches

        return -1  # Return -1 if needle is not found
        