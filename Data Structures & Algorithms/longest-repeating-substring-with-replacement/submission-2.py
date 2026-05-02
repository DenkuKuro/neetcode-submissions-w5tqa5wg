class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        charCount = [0] * 26
        longest = 0
        l = 0     
        for r in range(len(s)):
            charCount[ord(s[r]) - ord('A')] += 1
            maxCount = 0
            for c in charCount:
                maxCount = max(maxCount, c)
            while r - l + 1 - maxCount > k:
                charCount[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest