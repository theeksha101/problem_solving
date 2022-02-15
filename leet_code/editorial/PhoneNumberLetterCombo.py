from itertools import product
from typing import List


# RECURSIVE APPROACH

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []
        dict1 = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 1:
            return list(dict1[digits[0]])
        now = dict1[digits[0]]
        digits = digits[1:]
        after = self.letterCombinations(digits)
        ans = []
        for x in now:
            for y in after:
                ans.append(x + y)
        return ans


sol = Solution()
print(sol.letterCombinations("2356"))
print(sol.letterCombinations("23"))

# BACKTRACKING APPROACH

class Solution2:

    def rec(self, s, res, cand, pos, d):
        if len(cand) == len(s) and cand:
            res.append(cand)
            return
        for i in range(pos, len(s)):
            for char in d[s[i]]:
                self.rec(s, res, cand + char, i + 1, d)

    def letterCombinations(self, digits: str) -> List[str]:
        num_2_letters = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv",
                         '9': "wxyz"}
        res = []
        pos = 0
        self.rec(digits, res, "", pos, num_2_letters)
        return res


sol = Solution2()
sol.letterCombinations("23")
sol.letterCombinations("234")


# ITERATIVE ITERTOOLS APPROACH

class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # use dict for mapping values

        values = [mappings[c] for c in digits]
        res = []
        # use the product form itertools to omit the values in the sorted from

        for ele in product(*values):
            res.append(''.join(ele))

        if res != [""]:
            return res
        else:
            return []


sol = Solution3()
print(sol.letterCombinations("234"))
print(sol.letterCombinations(""))
