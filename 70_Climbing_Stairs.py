class Solution:
    def climbStairs(self, n: int) -> int:
        # fibo
        if n == 1:
            return 1
        previous_ways_1 = 1
        previous_ways_2 = 2
        for i in range(2, n):
            new = previous_ways_1 + previous_ways_2
            previous_ways_2 , previous_ways_1 = new , previous_ways_2
        return previous_ways_2
