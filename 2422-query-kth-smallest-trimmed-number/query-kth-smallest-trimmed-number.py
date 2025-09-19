class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for k,trim in queries:
            trimmed = [(num[-trim:],i) for i,num in enumerate(nums)]
            trimmed.sort(key= lambda x: (x[0],x[1]))
            ans.append(trimmed[k-1][1])
        return ans
        