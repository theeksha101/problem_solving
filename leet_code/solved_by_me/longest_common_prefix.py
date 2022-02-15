from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens_str = [len(i) for i in strs]
        print(lens_str)
        common_prefix = ''
        for i in range(min(lens_str)):
            for j in strs:
                while j[i] !=


sol = Solution()
sol.longestCommonPrefix(["flower", "flow", "flight"])
