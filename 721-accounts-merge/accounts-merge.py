class disjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [0]*n

    def findParent(self,node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return False
        elif self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = disjointSet(n)

        mailByNode = {}
        for i in range(n):
            for j in accounts[i][1:]:
                if j in mailByNode:
                    # mailByNode[j].append(i)
                    ds.unionBySize(i,mailByNode[j])
                else:
                    mailByNode[j] = i
        
        merged_mail = [[] for _ in range(n)]
        # print(mailByNode)
        for mail,node in mailByNode.items():
            parNode = ds.findParent(node)
            merged_mail[parNode].append(mail)
        # print(merged_mail)

        ans = []
        for i in range(n):
            if len(merged_mail[i])==0:
                continue
            merged_mail[i].sort()
            temp = []
            temp.append(accounts[i][0])
            for j in merged_mail[i]:
                temp.append(j)
            ans.append(temp)
        return ans


