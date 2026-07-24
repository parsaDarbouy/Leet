from typing import List


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        hierarchy_map = {}
        for region in regions:
            for i in range(len(region) - 1, 0, -1):
                if region[i] not in hierarchy_map:
                    if i == 0:
                        hierarchy_map[region[i]] = None
                    else:
                        hierarchy_map[region[i]] = region[0]
        temp = region1
        temp_map = {}
        while temp is not None:
            temp_map[temp] = temp
            temp = hierarchy_map.get(temp)
        temp = region2
        while temp is not None:
            if temp in temp_map:
                return temp
            temp = hierarchy_map.get(temp)
        return ""



def start():
    sol = Solution()
    earth = [
        ["Earth", "North America", "South America"],
        ["North America", "United States", "Canada"],
        ["United States", "New York", "Boston"],
        ["Canada", "Ontario", "Quebec"],
        ["South America", "Brazil"],
    ]
    cases = [
        # LeetCode example 1
        (earth, "Quebec", "New York", "North America"),
        # LeetCode example 2
        (earth, "Canada", "South America", "Earth"),
        # Direct siblings
        (earth, "United States", "Canada", "North America"),
        # Top-level siblings
        (earth, "North America", "South America", "Earth"),
        # One is ancestor of the other
        (earth, "United States", "Boston", "United States"),
        (earth, "Boston", "United States", "United States"),
        # Parent and direct child
        (earth, "Canada", "Ontario", "Canada"),
        # Deep leaf vs distant leaf
        (earth, "Boston", "Brazil", "Earth"),
        # Same region
        (earth, "Quebec", "Quebec", "Quebec"),
        # Minimal: two children under one parent
        ([["A", "B", "C"]], "B", "C", "A"),
        # Minimal: parent and child
        ([["A", "B"]], "A", "B", "A"),
        # Chain via nested lists
        ([["A", "B"], ["B", "C"], ["C", "D"]], "D", "B", "B"),
        ([["A", "B"], ["B", "C"], ["C", "D"]], "D", "C", "C"),
        ([["A", "B"], ["B", "C"], ["C", "D"]], "D", "A", "A"),
    ]
    failed = 0
    for regions, r1, r2, expected in cases:
        result = sol.findSmallestRegion(regions, r1, r2)
        ok = result == expected
        if not ok:
            failed += 1
        print(f"r1={r1!r}, r2={r2!r}")
        print(f"  got:      {result!r}")
        print(f"  expected: {expected!r}")
        print(f"  {'PASS' if ok else 'FAIL'}")
        print()
    print(f"{len(cases) - failed}/{len(cases)} passed")


if __name__ == "__main__":
    start()
