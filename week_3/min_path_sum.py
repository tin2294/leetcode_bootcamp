class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        # first column
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]

        # first row
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        # inner cells
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])

        return grid[-1][-1]


solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))