class Node:
    def __init__(self):
        self.links = [None,None]

    def get(self,ch):
        return self.links[ch]
    
    def contains(self,ch):
        return self.links[ch] is not None

    def put(self,ch,node):
        self.links[ch] = node

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,num):
        node = self.root
        for i in range(31,-1,-1):
            bit = (num>>i) & 1
            if not node.contains(bit):
                node.put(bit,Node())
            node = node.get(bit)

    def get_max(self,num):
        node = self.root
        maxi = 0
        for i in range(31,-1,-1):
            bit = (num>>i) & 1

            if node.contains(1-bit):
                maxi |= (1<<i)
                node = node.get(1-bit)
            else:
                node = node.get(bit)
        return maxi

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie()
        for i in nums:
            t.insert(i)
        ans = 0
        for i in nums:
            ans = max(ans,t.get_max(i))
        return ans