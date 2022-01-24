""" Reverting HALF NUMBER"""


class Solution:
    def is_palindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0
        while x > reversed_number:
            reversed_number = int(reversed_number * 10 + x % 10)
            x = int(x / 10)

        return x == reversed_number or x == int(reversed_number / 10)


inp = int(input())
sol = Solution()
is_palindrome = sol.is_palindrome(inp)
if is_palindrome:
    print("true", end="")
else:
    print("false", end="")

# lazy solution ::

# my solution with python3
# s = str(x)
# rs = "".join(list(reversed(s)))
# if rs != s:
#     return False
# return True
