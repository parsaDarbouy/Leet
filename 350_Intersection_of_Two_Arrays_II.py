class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            if i in ans:
                continue
            n = nums1.count(i)
            n_2 = nums2.count(i)
            count_i = min(n,n_2)
            ans = ans + ([i] * count_i)
        return ans
        
