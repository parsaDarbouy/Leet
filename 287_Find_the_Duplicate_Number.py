class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       dictionary = {}
       for x in nums:
            if x in dictionary:
                return x
            else:
                dictionary[x] = 1

