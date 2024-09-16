class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = 0
        first_time = True
        temp_val = None
        length = len(nums)
        if length == 1:
            return 1
        while pointer_2 < length:
            if temp_val is None:
                temp_val = nums[pointer_1]
                pointer_1 += 1
                pointer_2 += 1
                continue
            if temp_val == nums[pointer_2] and first_time:
                nums[pointer_1] = nums[pointer_2]
                pointer_1 += 1
                pointer_2 += 1
                first_time = False
                continue
            if temp_val == nums[pointer_2]:
                pointer_2 += 1
            else:
                first_time = True
                nums[pointer_1] = nums[pointer_2]
                temp_val = nums[pointer_1]
                pointer_1 += 1
                pointer_2 += 1

        return pointer_1
