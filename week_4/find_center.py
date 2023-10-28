from collections import Counter

class Solution:
    def findCenter(self, edges) -> int:
        flatlist = [num for edge in edges for num in edge]
        counts = Counter(flatlist)
        return max(counts, key=counts.get)
solution = Solution()
print(solution.findCenter([[1,2],[2,3],[4,2]]))