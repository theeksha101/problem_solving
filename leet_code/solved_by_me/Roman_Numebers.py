class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        temp = roman_dict[s[-1]]
        summation = temp
        for i in s[:-1][::-1]:
            value = roman_dict[i]
            if value >= temp:
                summation += value
                temp = value
            else:
                summation -= value

        return summation


sol = Solution()
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))  # 1000 = M + 900 = CM + 90 = XC + IV = 4
print(sol.romanToInt("III"))


