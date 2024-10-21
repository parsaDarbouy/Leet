class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        max_safe_int = 2**31 -1
        max_safe_int_negative = -2**31
        if s =="":
            return 0
        for d in range(len(s)):
            i = s[d]
            if i == ' ':
                continue
            if i == 0:
                continue
            elif i == '-':
                sign = 0
                break
            elif i == '+':
                break
            elif i in "1234567890":
                num += int(i)
                break
            else:
                return 0
        if sign:
            for j in s[d+1:]:
                if j in "1234567890":
                    num *= 10
                    num += int(j)
                else:
                    break
                if num > max_safe_int:
                    return max_safe_int
        else:
            for j in s[d+1:]:
                if j in "1234567890":
                    num *= 10
                    num -= int(j)
                else:
                    break
                if num<max_safe_int_negative:
                    return max_safe_int_negative
        
        return num

