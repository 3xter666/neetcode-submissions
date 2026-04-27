class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l1 = 0
        l2 = 0
        tmp = ""
        while l1 < len(s) and l2 < len(t):
            if(s[l1] == t[l2]):
                l2+=1
            l1+=1
        for i in range(l2,len(t)):
            tmp += t[l2]
        return len(tmp)
        
        