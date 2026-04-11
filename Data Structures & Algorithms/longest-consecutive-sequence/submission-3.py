class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        chset = set(nums)
        maxst = 0

        for num in nums:
            curr = num
            streak = 1
            while curr + 1 in chset:
                streak += 1
                curr += 1 
            maxst = max(streak, maxst)

        return maxst
                

        
      
        