class Solution(object):
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        sym_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        temp = sym_dict[s[-1]]
        sum_ = temp
        for i, sym in enumerate(s[:-1][::-1]):
            # Reads the string backwards starting from the second last
            val = sym_dict[sym]
            if val >= temp:
                sum_ += val
                temp = val
            else:
                sum_ -= val
        return sum_


sol = Solution()
print(sol.romanToInt("MCMXCIV"))  # 1000 = M + 900 = CM + 90 = XC + IV = 4
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))

