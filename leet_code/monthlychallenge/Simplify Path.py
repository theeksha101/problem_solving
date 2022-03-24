# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         canon_path = []
#         word = ""
#         i = 0
#         if len(path) == 0:
#             return ""
#         while i in range(len(path)):
#             if path[i] != "/" and path[i] != ".":
#                 while path[i] != "/":
#                     word = word + path[i]
#                     i += 1
#                 canon_path.append("/" + word)
#                 word = ""
#                 i -= 1
#             elif canon_path and path[i] == ".":
#                 canon_path.pop()
#             i += 1
#         canon_string = "".join(canon_path)
#         if not canon_string:
#             return "/"
#         else:
#             return canon_string

# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         # split it based on /
#         # Though it increases space complexity of the solution, it eases the implementation.
#         # Hence, it is a decent trade off
#         arr = path.split("/")
#         out = ""
#         # iterate through every substring
#         for sub in arr:
#             # remove the previous directory from out when .. is encountered
#             if sub == ".." and len(out) > 0:
#                 out = out[:out.rindex('/')]
#             # ignore ".", "..", "" and add rest to output
#             elif sub not in (".", "", ".."):
#                 out += ("/" + sub)
#
#         # finally make sure to add "/" if result is empty
#         return out if len(out) > 0 else "/"
class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        out = ""
        for char in split_path:
            if char == ".." and len(out) > 0:
                out = out[:out.rindex("/")]
            elif char not in ("", ".", ".."):
                out = out + ("/" + char)
        return out if len(out) > 0 else "/"


# Time Complexity, Space Complexity : O(N)
# Such a small problem statement has so many edge cases to cover. How fascinating :-)


sol = Solution()
print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/../"))
print(sol.simplifyPath(""))
print(sol.simplifyPath("/a/./b/../../c/"))
print(sol.simplifyPath("/a/../../b/../c//.//"))
