class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ls = sum(cardPoints[0:k])
        rs = 0
        ans = ls
        for i in range(k):
            ls -= cardPoints[k-i-1]
            rs += cardPoints[len(cardPoints)-1-i]
            ans = max(ans,ls+rs)
        return ans