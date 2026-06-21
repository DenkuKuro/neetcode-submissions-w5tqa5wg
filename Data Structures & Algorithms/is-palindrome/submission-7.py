class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLowered = s.casefold()
        def isAlphNum(c):
            return 'a' <= c <= 'z' or '0' <= c <= '9'

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isAlphNum(sLowered[l]):
                l += 1
            while l < r and not isAlphNum(sLowered[r]):
                r -= 1
            if sLowered[l] != sLowered[r]:
                return False
            l += 1
            r -= 1
        return True
        
