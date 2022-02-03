class Solution:
    def len_of_longest_substring(self, s: str) -> int:
        substring = []
        len_substring = 0
        len_string = len(s)
        k = 0

        for i in range(len_string):
            for j in range(k, len_string):
                if s[j] in substring:
                    substring.clear()
                    k += 1
                    break
                substring.append(s[j])
                if len_substring < len(substring):
                    len_substring = len(substring)

        return len_substring


sol = Solution()
print(sol.len_of_longest_substring("abcabcdef"))
