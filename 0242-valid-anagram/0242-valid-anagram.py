class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same length
        if len(s) != len(t):
            return False

        # Sort both strings and compare
        return sorted(s) == sorted(t)
                    
        