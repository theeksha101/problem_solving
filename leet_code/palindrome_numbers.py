class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        original = x
        while x != 0:
            remainder = int(x % 10)
            reverse = int(reverse * 10 + remainder)
            x = int(x / 10)
        if original == reverse:
            return True
        else:
            return False


inp = int(input())
sol = Solution()
is_palindrome = sol.isPalindrome(inp)
if is_palindrome:
    print("true", end="")
else:
    print("false", end="")
