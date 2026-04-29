class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_seq = 0
        for n in nums:
            cur_seq = 1
            if n - 1 in s:
                continue
            next_n = n + 1
            while next_n in s:
                cur_seq += 1
                next_n += 1
            longest_seq = max(longest_seq, cur_seq)
        return longest_seq
        
        

            
            
