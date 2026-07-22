from typing import List


class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            pour_index = k
            while True:
                if pour_index == 0:
                    break
                if pour_index == len(heights) - 1:
                    break
                if heights[pour_index] > heights[pour_index - 1]:
                    pour_index -= 1
                elif heights[pour_index] > heights[pour_index + 1]:
                    pour_index += 1
                else:
                    break
            heights[pour_index] += 1
        return heights


def start():
    sol = Solution()
    cases = [
        ([2, 1, 1, 2, 1, 2, 2], 4, 3, [2, 2, 2, 3, 2, 2, 2]),
        ([1, 2, 3, 4], 2, 2, [2, 3, 3, 4]),
        ([3, 1, 3], 5, 1, [4, 4, 4]),
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
