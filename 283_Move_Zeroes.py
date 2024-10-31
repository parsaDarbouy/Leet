class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i= 0 
        count = 0
        while i < length:
            if nums[i] == 0:
                nums [:] = nums[:i] + nums[i+1:]
                length -= 1
                count += 1
            else:
                i += 1
        for i in range(count):
            nums.append(0)
        return nums
