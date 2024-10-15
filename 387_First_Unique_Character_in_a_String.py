class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = {}
        for i in s:
            dictionary[i] = dictionary.get(i,0) + 1

        for i,char in enumerate(s):
            if dictionary[char]==1:
                return i
        return -1
