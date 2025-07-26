class Node:
    def __init__(self):
        self.links = [None,None]

    def contains(self,bit):
        return self.links[bit] is not None

    def get(self,bit):
        return self.links[bit]

    def put(self,bit,node):
        self.links[bit] = node

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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        mp = []
        for i in range(len(queries)):
            mp.append([queries[i][1],queries[i][0],i])
        mp.sort(key = lambda x: x[0])
        print(mp)
        trie = Trie()
        ans = [-1]*len(queries)
        ind = 0
        for i in range(len(mp)):
            while ind<len(nums) and nums[ind]<= mp[i][0]:
                trie.insert(nums[ind])
                ind += 1
            if ind != 0:
                ans[mp[i][2]] = trie.get_max(mp[i][1])
        return ans