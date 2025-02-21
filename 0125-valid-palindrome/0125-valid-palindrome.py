class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and filter out non-alphanumeric characters
        s = "".join([char.lower() for char in s if char.isalnum()])

        # Check if the cleaned string is equal to its reverse
        return s == s[::-1]

        