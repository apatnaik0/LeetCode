class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        f = len(fruits)
        b = len(baskets)
        vis = [False]*b
        unplaced = f
        for i in range(f):
            for j in range(b):
                # print(fruits[i],baskets[j])
                if baskets[j]>=fruits[i] and not vis[j]:
                    # print('inside if')
                    unplaced -=1
                    vis[j] = True
                    # print(unplaced,vis)
                    break
        return unplaced