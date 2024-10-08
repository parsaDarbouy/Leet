# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return bin_find(1,n)

def bin_find(s,f):
    mid = (s+f)//2
    if isBadVersion(mid):
        if not isBadVersion(mid -1):
            return mid
        if mid == f:
            mid -= 1
        return bin_find(s,mid)
    else:
        if mid == s:
            mid += 1
        return bin_find(mid,f)

