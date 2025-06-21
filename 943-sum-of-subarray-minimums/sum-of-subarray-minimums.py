class Solution:
    def Nse(self, arr):
        n = len(arr)
        nse = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            nse[i] = n if not stack else stack[-1]
            stack.append(i)
        return nse

    def Pse(self, arr):
        n = len(arr)
        pse = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            pse[i] = -1 if not stack else stack[-1]
            stack.append(i)
        return pse

    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = self.Nse(arr)
        pse = self.Pse(arr)
        total = 0
        mod = int(1e9 + 7)
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + arr[i] * left * right) % mod
        return total