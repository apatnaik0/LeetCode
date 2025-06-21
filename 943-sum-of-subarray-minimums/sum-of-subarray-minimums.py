class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        n = len(arr)
        stack = []
        prev_smaller = [-1]*n
        next_smaller = [n]*n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                next_smaller[index] = i
            stack.append(i)

        ans = sum((i-prev_smaller[i]) * (next_smaller[i] - i) * arr[i] for i in range(n))%MOD

        return ans