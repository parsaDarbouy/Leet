class Solution:
    def rob(self, nums: List[int]) -> int:
        table = [[0, 0]]
        for i in range(len(nums)):
            breaking = max(table[i - 1][0], table[i - 1][1]) + nums[i]
            leaving = max(table[i][0], table[i][1])
            table.append([breaking, leaving])
        return max(table[-1][0], table[-1][1])
