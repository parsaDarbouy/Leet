class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        end_pointer = length - 1
        flag = 1
        while k <= end_pointer:
            if nums[k] == val:
                if nums[end_pointer] == val:
                    end_pointer -= 1
                    continue
                else:
                    nums[k] = nums[end_pointer]
                    flag = 0
                    k += 1
                    end_pointer -= 1
            else:
                flag = 0
                k += 1
        if flag:
            k = 0
            return k
        return k 
