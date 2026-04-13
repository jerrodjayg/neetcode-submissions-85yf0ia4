class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        captech = set(nums)

        for num in nums:
            if num - 1 not in captech:
                length = 1
                while num + length in captech:
                    length += 1

                longest = max(length, longest)

        return longest


        