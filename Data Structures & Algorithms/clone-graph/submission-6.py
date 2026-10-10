"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        if node is None: return None

        def dfs(old):
            if old in old_to_new:
                return old_to_new[old]

            new = Node(old.val)
            old_to_new[old] = new

            for old_nei in old.neighbors:
                new_nei = dfs(old_nei)
                new.neighbors.append(new_nei)

            return new

        head = dfs(node)
        return head

