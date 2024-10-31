class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        length = len(needle)
        while (i+length) <= len(haystack):
            if haystack[i:i+length] == needle:
                return i
            i += 1
        return -1
