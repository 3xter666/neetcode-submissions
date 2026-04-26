class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = 0
        i = 0
        while i < len(t) and check < len(s):
            if(s[check] == t[i]):
                check += 1
            i += 1
        return check == len(s)