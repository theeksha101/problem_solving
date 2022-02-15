class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        num = 0
        sign = 1
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31

        while s[index] == ' ' and index < len(s):
            index += 1
            if index < len(s):
                break

        if s[index] == '-':
            sign = -1
            index += 1

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if num > max_int // 10 or num == max_int // 10 and digit > max_int % 10:
                return max_int if sign == 1 else min_int

            num = 10 * num + digit
            index += 1

        return sign * num


sol = Solution()
# print(sol.myAtoi(''))
print(sol.myAtoi(' '))
print(sol.myAtoi("21474836460"))
print(sol.myAtoi('jfkdla890'))
print(sol.myAtoi('890'))
print(sol.myAtoi('-890'))
print(sol.myAtoi('    -890'))
print(sol.myAtoi(' -890a90'))
print(sol.myAtoi(' -890 90'))
print(sol.myAtoi(' -8905698321456987856590'))
print(sol.myAtoi('8905698321456987856590'))

