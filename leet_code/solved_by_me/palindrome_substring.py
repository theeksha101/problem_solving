class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome_dict = {}
        longest_palindrome = ""
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            for j in range(2, len(s) + 1):
                is_pal = self.is_palindrome(s[i:j])
                if is_pal and len(s[i:j]) > len(longest_palindrome):
                    longest_palindrome = s[i:j]
                # elif len(s[i:j]) > len(longest_palindrome):
                #     longest_palindrome = s[i:j]
        # print(palindrome_dict)
        # if len(palindrome_dict) == 0:
        #     return ""
        # # else:
        # max_value = max(palindrome_dict.values())
        # return list(palindrome_dict.keys())[list(palindrome_dict.values()).index(max_value)]
        if len(longest_palindrome) == 0:
            return s[0]
        else:
            return longest_palindrome

    def is_palindrome(self, string: str) -> bool:
        if string[::-1] == string:
            return True
        else:
            return False


sol = Solution()
print(sol.longestPalindrome("dc"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("abba"))
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome("ababa"))
print(sol.longestPalindrome("babad"))
