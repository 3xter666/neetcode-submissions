class Solution:
    def isHappy(self, n: int) -> bool:
        mp = {}
        while(n):
            total = 0
            while n:
                total += (n % 10) ** 2
                n = n // 10
            if total in mp:
                break
            mp[total] = 1
            if(total == 1):
                return True
            n = total
        return False