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
        return bin_find(s,mid)
    else:
        return bin_find(mid+1,f)

