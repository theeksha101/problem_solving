class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)


class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(abs(x))

        reversed = int(s[::-1])

        if reversed > 2147483647:
            return 0

        return reversed if x > 0 else (reversed * -1)
