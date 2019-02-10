#two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in dic:
                return [i,dic[rest]]
            else:
                dic[nums[i]] = i