class Solution:
    def __init__ (self):
        self.result = []
    def recursive_count(self,nums):
        if len(nums) == 1:
            #self.result.update({1:nums[0]})
            self.result.append(1)
        else:
            self.recursive_count(nums[:-1])
            current_value = [1]
            for i in range(len(nums)-1):
                if nums[-1] > nums[i]:
                    current_value.append(self.result[i] + 1)
            self.result.append(max(current_value))
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        self.recursive_count(nums)
        length = max(self.result)
        self.result = []
        return length
        """
        :type nums: List[int]
        :rtype: int
        """
