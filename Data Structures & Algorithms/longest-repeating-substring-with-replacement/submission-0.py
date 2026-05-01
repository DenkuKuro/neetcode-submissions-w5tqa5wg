class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        charCount = [0] * 26
        for r in range(len(s)):
            charCount[ord(s[r]) - ord('A')] += 1
            maxFChar = 0
            for c in charCount:
                maxFChar = max(maxFChar, c)
            while r - l + 1 - maxFChar > k:
                charCount[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)


        return longest        