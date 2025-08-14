class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ''
        for i in range(1,n-1):
            if num[i-1]==num[i] and num[i]==num[i+1]:
                if ans < num[i-1:i+2]:
                    ans = num[i-1:i+2]
        return ans
        