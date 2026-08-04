class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            res += str(n) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            n = ""
            while s[i] != '#':
                n += s[i]
                i += 1
            i += 1
            end = i + int(n)
            cur_s = ""
            while i < len(s) and i < end:
                cur_s += s[i]
                i += 1
            res.append(cur_s)
        return res                