class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC":90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "MD": 900,
            "M": 1000
        }
        roman_list = []
        for k, v in reversed(roman_dict.items()):
            while num > 0:
                if v <= num:
                    roman_list.append(k)
                    num -= v
                else:
                    break
        return "".join(roman_list)


sol = Solution()
print(sol.intToRoman(1994))


class Solution3:

    def intToRoman(self, num: int) -> str:
        roman = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
                 ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        result = ''
        for key, value in reversed(roman):
            if num // value:
                count = num // value
                result += (count * key)
                num = num % value
        return result


sol3 = Solution3()
print(sol3.intToRoman(625))


class Solution4:

    def intToRoman(self, num: int) -> str:
        roman_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "MD": 900,
            "M": 1000
        }
        result = ''
        for key, value in reversed(roman_dict.items()):
            if num // value:
                count = num // value
                result += (count * key)
                num = num % value
        return result


sol3 = Solution4()
print(sol3.intToRoman(625))
