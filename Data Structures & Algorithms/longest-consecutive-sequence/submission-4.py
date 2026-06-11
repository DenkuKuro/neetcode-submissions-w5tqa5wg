class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in nums:
            cur_len = 1
            if n - 1 in nums:
                continue
            
            next_n = n + 1
            while next_n in seen:
                cur_len += 1
                next_n += 1
            res = max(res, cur_len)
        return res
        

            
            
