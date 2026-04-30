class Solution:
    def romanToInt(self, s: str) -> int:
        a = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M':1000,
        }
        res = 0
        before = 0
        for i in s:
            if a[i] > before:
                res += a[i] - before * 2
            else:
                res += a[i]
            before = a[i]
        return res