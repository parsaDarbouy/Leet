class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        temp = 1
        length = len(digits)
        while temp:
            digits[index] += temp
            if digits[index] == 10:
                digits[index] = 0
                temp = 1
            else:
                temp = 0

            if index <= -length:
                if digits[0] == 0:
                    digits[0] = 0
                    digits = [1] + digits
                break
            index -= 1

        return digits
        
