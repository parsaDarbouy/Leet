class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for i in nums:
            if count == 0:
                majority = i
                count += 1
            elif i == majority:
                count += 1
            else:
                count -= 1
        return majority
