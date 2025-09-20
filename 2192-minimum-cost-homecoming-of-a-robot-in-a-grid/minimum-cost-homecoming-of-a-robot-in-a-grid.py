class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0
        if startPos[0]<homePos[0]:
            for i in range(startPos[0]+1,homePos[0]+1):
                ans += rowCosts[i]
        else:
            for i in range(homePos[0],startPos[0]):
                ans += rowCosts[i]

        if startPos[1]<homePos[1]:
            for i in range(startPos[1]+1,homePos[1]+1):
                ans += colCosts[i]
        else:
            for i in range(homePos[1],startPos[1]):
                ans += colCosts[i]
        return ans