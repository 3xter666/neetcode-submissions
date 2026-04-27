class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l1 = 0
        l2 = 0
        while l2 < len(s):
            if s[l2] == t[l1]:
                l1 += 1
                if l1 == len(t):
                    return 0
            l2 += 1
        return len(t) - l1
        
        