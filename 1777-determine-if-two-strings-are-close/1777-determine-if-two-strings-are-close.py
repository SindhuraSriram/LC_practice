from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If the sets of unique characters in word1 and word2 are not equal, return False
        if set(word1) != set(word2):
            return False

        # Compare sorted frequency counts
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
