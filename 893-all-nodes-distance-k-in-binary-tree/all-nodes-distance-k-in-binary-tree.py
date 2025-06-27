# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def getParents(root):
            parlist = {}
            q = deque()
            q.append(root)
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        parlist[node.left]=node
                        q.append(node.left)
                    if node.right:
                        parlist[node.right]=node
                        q.append(node.right)
            return parlist
        
        parlist = getParents(root)
        # print(parlist)
        visited = []
        q = deque()
        q.append(target)
        visited.append(target)
        while q:
            # print(q,k)
            if k==0:
                break
            for i in range(len(q)):
                # print(q)
                node = q.popleft()
                # print(node,visited)
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.append(node.right)
                if node in parlist and parlist[node] not in visited:
                    q.append(parlist[node])
                    visited.append(parlist[node])
                # print(q,visited)
            k-=1
        # print(q)
        ans = []
        while q:
            ans.append(q.popleft().val)
        return ans
