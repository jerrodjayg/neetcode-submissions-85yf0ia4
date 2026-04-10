class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ctset = set()

        for num in nums:
            if num in ctset:
                return True
            ctset.add(num)
        return False 