class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = nums.copy()
        for i in nums:
            a.append(i)
        return a