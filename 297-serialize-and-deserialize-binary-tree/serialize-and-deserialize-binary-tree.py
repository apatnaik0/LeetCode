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
            return ''
        s = ''
        q = deque()
        q.append(root)
        s += str(root.val) + ','
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    s += str(node.left.val) + ','
                else:
                    s += '#' + ','
                if node.right:
                    q.append(node.right)
                    s += str(node.right.val) + ','
                else:
                    s += '#' + ','
        return s[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        s = data.split(',')
        root = TreeNode(s.pop(0))
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                l = s.pop(0)
                if l!='#':
                    new = TreeNode(l)
                    node.left = new
                    q.append(new)
                
                r = s.pop(0)
                if r!='#':
                    new = TreeNode(r)
                    node.right = new
                    q.append(new)
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))