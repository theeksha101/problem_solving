class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            x = n * (2 * n - 1)
            y = self.countOrders(n - 1)
            z = (x * y) % (10 ** 9 + 7)
            return z


sol = Solution()
print(sol.countOrders(3))
