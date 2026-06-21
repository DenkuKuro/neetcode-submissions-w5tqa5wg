class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in s:
                cur_longest = 1
                next_n = n + 1
                while next_n in s:
                    next_n += 1
                    cur_longest += 1
                longest = max(longest, cur_longest)
        return longest
                

            
            
