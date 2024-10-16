class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        temp = 1
        while temp <= n:
            if n == temp:
                return True
            else:
                temp *= 3

        return False

