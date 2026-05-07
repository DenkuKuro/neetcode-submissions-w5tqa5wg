class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        longest = 0
        l = 0
        count = [0] * 26
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            maxChar = 0
            for c in count:
                maxChar = max(maxChar, c)
            while r - l + 1 - maxChar > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
