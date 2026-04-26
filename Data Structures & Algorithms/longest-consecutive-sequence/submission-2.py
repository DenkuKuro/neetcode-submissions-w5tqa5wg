class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for n in nums:
            if n - 1 in s:
                continue
            cur_seq = 1
            next_num = n + 1
            while next_num in s:
                next_num += 1
                cur_seq += 1
            longest = max(longest, cur_seq)
        return longest
        

            
            
