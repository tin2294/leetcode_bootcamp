from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        answer = []
        # put root into the queue
        if root != None:
            queue.append(root)
        
        # go through the queue
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                if isinstance(node,TreeNode):
                    answer.append(node.val)
                    if node.left != None:
                        queue.append(node.left)
                    if node.right != None:
                        queue.append(node.right)
                else:
                    answer.append(node)
        answer.sort()
        return answer[k-1]


solution = Solution()
print(solution.kthSmallest(root=TreeNode(val=3, left=TreeNode(val=1, left=None, right=2), right=4), k=1))


