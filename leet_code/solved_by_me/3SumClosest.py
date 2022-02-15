from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini_diff = float("inf")

        for i in range(len(nums) - 2):
            left_pointer = i + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                three_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                diff = target - three_sum

                if diff == 0:
                    return target

                if abs(diff) < abs(mini_diff):
                    mini_diff = diff

                if diff > 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return target - mini_diff
