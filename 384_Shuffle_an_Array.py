import random
import copy
class Solution:

    def __init__(self, nums: List[int]):
        self.original_list = nums
        

    def reset(self) -> List[int]:
        return self.original_list
        

    def shuffle(self) -> List[int]:
        n = len(self.original_list)
        temp = self.original_list.copy()
        for i in range(n):
            rand = random.randint(i,n-1)
            temp[i],temp[rand] = temp[rand],temp[i]
        return temp
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
