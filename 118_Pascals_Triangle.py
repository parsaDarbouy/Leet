class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        i = 2
        while i < numRows:
            ans.append([1])
            for j in range(len(ans[-2])):
                if j+1 < len(ans[-2]):
                    ans[-1].append(ans[-2][j]+ ans[-2][j+1])
            ans[-1].append(1)
            i += 1
        return ans

