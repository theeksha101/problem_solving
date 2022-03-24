from typing import List


class Solution1:
    def countBits(self, num):
        arr = [0]

        for i in range(1, num + 1):
            arr.append(arr[i >> 1] + (i & 1))

        return arr


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            if (i % 2) == 0:
                res[i] = res[i >> 1]
            else:
                res[i] = res[i >> 1] + 1
        return res


sol = Solution()
print(sol.countBits(5))
