class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer_1 = m - 1
        pointer_2 = n - 1
        if nums2:
            for i in range(len(nums1), 0, -1):
                if pointer_1 < 0:
                    nums1[i-1] = nums2[pointer_2]
                    pointer_2 -= 1
                    continue
                if nums1[pointer_1] > nums2[pointer_2]:
                    nums1[i-1] = nums1[pointer_1]
                    pointer_1 -= 1
                else:
                    nums1[i-1] = nums2[pointer_2]
                    pointer_2 -= 1
                if pointer_2 < 0:
                    break
