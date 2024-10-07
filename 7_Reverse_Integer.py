class Solution:
    def reverse(self, x: int) -> int:
        negative = 0
        if x < 0:
            negative = 1
        digits = []
        x = abs(x)
        while x != 0:
            first_digit = x % 10
            digits.append(first_digit)
            x = x // 10
        rev_number = 0
        co = 1
        for i in digits[::-1]:
            rev_number += (i * co)
            co *= 10
        if negative:
            rev_number *= -1
        if rev_number > ((2**31) -1) or rev_number < -(2**31):
            return 0
        return rev_number

