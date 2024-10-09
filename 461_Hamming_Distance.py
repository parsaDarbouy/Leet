class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while True:
            if x != 0:
                x_remainder = x % 2
            else:
                x_remainder = 0
            if y != 0:
                y_remainder = y % 2
            else: 
                y_remainder = 0
            if x_remainder != y_remainder:
                distance += 1
            x = x >> 1
            y = y >> 1
            if not (x or y):
                break
        return distance
