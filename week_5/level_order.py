# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        queue = deque()
        answer = []
        # put root into the queue
        if root != None:
            queue.append(root)
        # go through the queue
        while len(queue) > 0:
            pair = []
            for _ in range(len(queue)):
                node = queue.popleft()
                pair.append(node.val)
                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)
            answer.append(pair)
        return answer

        
solution = Solution
node = TreeNode(val= 3, left= TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None), right=TreeNode(val=7, left=None, right=None)))
print(solution.levelOrder(0,node))