from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                min_height = min(height[i], height[j])
                max_area = max(max_area, min_height * (j - i))
        return max_area


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            min_height = min(height[l], height[r])
            max_area = max(max_area, min_height * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


sol = Solution2()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
