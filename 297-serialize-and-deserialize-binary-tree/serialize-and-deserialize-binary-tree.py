# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
                
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = ""
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    ans += '#,'
                else:
                    ans += str(node.val) + ','
                    q.append(node.left)
                    q.append(node.right)
        return ans
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        nodes = data.split(',')
        root = TreeNode(nodes.pop(0))
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                left = nodes.pop(0)
                if left!='#':
                    newnode = TreeNode(left)
                    node.left = newnode
                    q.append(newnode)

                right = nodes.pop(0)
                if right!='#':
                    newnode = TreeNode(right)
                    node.right = newnode
                    q.append(newnode)
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))