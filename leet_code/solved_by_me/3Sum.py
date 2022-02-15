from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        len_nums = len(nums)
        list_nums = []

        if len_nums > 3:
            for i in range(len_nums - 2):
                for j in range(i + 1, len_nums - 1):
                    k = j + 1
                    triplets = [nums[i], nums[j], nums[k]]
                    triplets.sort()
                    if sum(triplets) == 0:
                        if triplets not in list_nums:
                            list_nums.append(triplets)
            return list_nums
        elif len_nums == 3 and sum(nums) == 0:
            list_nums.append(nums)
            return list_nums
        else:
            return []


sol = Solution()
print(sol.threeSum([-2, 0, 1, 1, 2]))
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))

print(sol.threeSum([0]))
print(sol.threeSum([]))
