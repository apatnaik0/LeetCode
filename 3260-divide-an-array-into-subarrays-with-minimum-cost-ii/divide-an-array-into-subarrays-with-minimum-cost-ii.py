class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        pq_used, pq_unused, used = [], [], set()
        s, ans = 0, float('inf')
        n = len(nums)

        for r in range(1,n):
            l = r - dist - 1

            if l>0 and l in used:
                used.remove(l)
                s -= nums[l]

                while pq_unused and pq_unused[0][1] < l:
                    heappop(pq_unused)
                
                if pq_unused:
                    num, i = heappop(pq_unused)
                    used.add(i)
                    heappush(pq_used,(-num,i))
                    s += num
            
            if len(used) < k-1:
                used.add(r)
                heappush(pq_used,(-nums[r],r))
                s += nums[r]
            else:
                while pq_used[0][1] not in used:
                    heappop(pq_used)

                if nums[r] < -pq_used[0][0]:
                    num, i = heapreplace(pq_used,(-nums[r],r))
                    used.remove(i)
                    used.add(r)
                    s += num + nums[r]
                    heappush(pq_unused, (-num,i))
                else:
                    heappush(pq_unused,(nums[r],r))
            
            if l >= 0:
                ans = min(s,ans)

        return nums[0]+ans
