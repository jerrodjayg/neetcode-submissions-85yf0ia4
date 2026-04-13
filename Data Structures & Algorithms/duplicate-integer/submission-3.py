class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        captech = set()

        for num in nums:
            if num in captech:
                return True
            captech.add(num)
        
        return False 
        