class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ctset = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in ctset:
                length = 1
                while num + length in ctset:
                    length += 1
            
                longest = max(length, longest)


        return longest 

        
    