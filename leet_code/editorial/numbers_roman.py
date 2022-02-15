class Solution:
    def intToRoman(self, num: int) -> str:
        a = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        c = []
        for k, v in reversed(a.items()):
            while num > 0:
                if v <= num:
                    c.append(k)
                    num -= v
                else:
                    break
        return "".join(c)


sol = Solution()
print(sol.intToRoman(1994))
print(sol.intToRoman(562))
print(sol.intToRoman(42))
print(sol.intToRoman(724))
print("59 -> ", sol.intToRoman(59))


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


class Solution2:
    def intToRoman(self, num: int) -> str:
        symbol_map = {1: 'I',
                      5: 'V',
                      10: 'X',
                      50: 'L',
                      100: 'C',
                      500: 'D',
                      1000: 'M'}
        res = (num // 1000) * symbol_map[1000]
        num %= 1000

        div = 100
        while div:
            div_count = num // div
            div_symbol, divx5_symbol = symbol_map[div], symbol_map[div * 5]

            if div_count == 4:
                res += div_symbol + divx5_symbol
            elif div_count == 9:
                res += div_symbol + symbol_map[div * 10]
            else:
                res += ((div_count >= 5) * divx5_symbol) + ((div_count % 5) * div_symbol)

            num %= div
            div //= 10

        return res
