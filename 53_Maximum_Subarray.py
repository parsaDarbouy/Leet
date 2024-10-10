class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = nums[0]
        max_s = nums[0]
        for i,x in enumerate(nums[1:]):
            if (sums + x) < 0:  
                sums = x
                max_s = max(max_s,sums)
            else:
                if sums < 0 :
                    sums = 0
                sums += x
                max_s = max(max_s,sums) 
        return max_s
            
