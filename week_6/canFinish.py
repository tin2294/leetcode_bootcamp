from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # flat_list = [item for sublist in prerequisites for item in sublist]
        # unique_values = list(set(flat_list))
        indegree = [0] * numCourses
        adj = [[] for x in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return numCourses == visited

solution = Solution
# print(solution.canFinish(0, numCourses = 2, prerequisites = [[1,0]]))
print(solution.canFinish(0, numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
# print(solution.canFinish(0, numCourses = 2, prerequisites = [[1,0],[0,1]]))