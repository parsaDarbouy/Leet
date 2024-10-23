class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        pre = ""
        for i in strs:
            if i == "":
                return pre
        
        while True:
            if index > (len(strs[0]) - 1):
                return pre
            letter = strs[0][index]
            for i in strs[1:]:
                if index > (len(i) - 1):
                    return pre
                print("checking",i,':',i[index])
                if letter != i[index]:
                    return pre
            index += 1
            pre += letter

