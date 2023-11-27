class Solution:
    def findMinArrowShots(self, points) -> int:
        points = sorted(points)
        min_right = points[0][1]
        ans = 1
        if len(points) > 1:
            for b in points[1:]:
                if min_right >= b[0]:
                    min_right = min(min_right, b[1])
                else:
                    ans+=1
                    min_right = b[1]
        return ans     
        
solution = Solution()
print(solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))


