from typing import List


class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            # Prefer left: walk downhill (including flats), settle on lowest
            best = k
            i = k
            while i > 0 and heights[i] >= heights[i - 1]:
                i -= 1
                if heights[i] < heights[best]:
                    best = i
            if best != k:
                heights[best] += 1
                continue

            # Otherwise try right the same way
            best = k
            i = k
            while i < len(heights) - 1 and heights[i] >= heights[i + 1]:
                i += 1
                if heights[i] < heights[best]:
                    best = i
            heights[best] += 1
        return heights


def start():
    sol = Solution()
    cases = [
        ([2, 1, 1, 2, 1, 2, 2], 4, 3, [2, 2, 2, 3, 2, 2, 2]),
        ([1, 2, 3, 4], 2, 2, [2, 3, 3, 4]),
        ([3, 1, 3], 5, 1, [4, 4, 4]),
        ([1, 0, 1], 1, 0, [1, 1, 1]),
        ([0, 1], 1, 1, [1, 1]),
        ([4, 4, 4, 2], 1, 0, [4, 4, 4, 3]),
    ]
    for heights, volume, k, expected in cases:
        result = sol.pourWater(heights[:], volume, k)
        print(f"heights={heights}, V={volume}, K={k}")
        print(f"  got:      {result}")
        print(f"  expected: {expected}")
        print(f"  {'PASS' if result == expected else 'FAIL'}")
        print()


if __name__ == "__main__":
    start()
