class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")]}":
                if stack == []:
                    return False
                temp = stack.pop()
                if temp == "(" and i != ")":
                    return False
                elif temp == "{" and i != "}":
                    return False
                elif temp == "[" and i != "]":
                    return False
        if stack != []:
            return False
        return True
                
        
