class Solution:
    def isPalindrome(self, s: str) -> bool:
             
        def isAlphaNum(c):
            return 'a' <= c <= 'z' or '0' <= c <= '9'
        newS = s.casefold()
        l = 0
        r = len(newS) - 1
        while l <= r:
            while l < r and not isAlphaNum(newS[l]):
                l += 1
            while l < r and not isAlphaNum(newS[r]):
                r -= 1
            if newS[l] !=  newS[r]:
                return False
            l += 1
            r -= 1

        return True