class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ct = 0
        rem_map = defaultdict(int)
        psum = 0
        rem_map[0] += 1 

        for i in nums:
            psum += i
            rem = psum % k
            if rem < 0:
                rem += k
            if rem in rem_map:
                ct += rem_map[rem]
            rem_map[rem] += 1
        return ct
