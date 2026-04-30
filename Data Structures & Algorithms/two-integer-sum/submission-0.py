class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i in range(len(nums)):
            tmp_num = target - nums[i]
            if tmp_num in tmp:
                return [tmp[tmp_num],i]
            tmp[nums[i]] = i
        return None