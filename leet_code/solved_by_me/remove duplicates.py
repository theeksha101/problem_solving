from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # try:
        #     i = 0
        #     while i in range(len(nums)):
        #         if nums[i] == nums[i + 1]:
        #             nums.remove(nums[i])
        #             i -= 1
        #         i += 1
        # except IndexError:
        #     pass
        nums = list(set(nums))
        return nums


sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(sol.removeDuplicates([1, 1, 2]))
