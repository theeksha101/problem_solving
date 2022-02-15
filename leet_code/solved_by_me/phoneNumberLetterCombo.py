from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        letters = [phone_dict[i] for i in digits]

        list_combo = []
        for i in product(*letters):
            list_combo.append(''.join(i))
        return list_combo


sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))


class Solution2:
    def letterCombinations(self, str_digit):
        if not str_digit or len(str_digit) == 0:
            return []
        dict1 = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(str_digit) == 1:
            return list(dict1[str_digit[0]])
        now = dict1[str_digit[0]]
        new_digit = str_digit[1:]
        after = self.letterCombinations(new_digit)
        combo = []
        for x in now:
            for y in after:
                combo.append(x + y)
        return combo


sol = Solution2()
print(sol.letterCombinations("23"))
print(sol.letterCombinations("234"))
print(sol.letterCombinations(""))