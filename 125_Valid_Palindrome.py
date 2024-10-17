class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_1 = 0
        p_2 = len(s) - 1

        while p_1 < p_2:
            print(str(p_1) + "----" + str(p_2))
            if ('a' <= s[p_1].lower() <= 'z' or s[p_1] in "1234567890") and ('a' <= s[p_2].lower() <= 'z' or s[p_2] in "1234567890"):
                if s[p_1].lower() != s[p_2].lower():
                    return False
                else:
                    p_1 += 1
                    p_2 -= 1
                    continue
            else:
                if not ('a' <= s[p_1].lower() <= 'z' or s[p_1] in "1234567890"):
                    p_1 += 1
                if not ('a' <= s[p_2].lower() <= 'z' or s[p_2] in "1234567890"):
                    p_2 -= 1
                
        return True
                
            
