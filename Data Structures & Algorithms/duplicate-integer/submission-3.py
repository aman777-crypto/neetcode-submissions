class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:


        count = {}


        for i in range(len(nums)):
            if nums[i] in count:
                return True
            else:
                count[nums[i]] = count.get(nums[i],0) +1
        return False
