class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            remainder = n % 2
            if remainder == 1:
                count += 1
            n = n >> 1
        return count
