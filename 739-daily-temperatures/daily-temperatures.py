class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        ans = [0]*n

        for i,temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                index = st.pop()
                ans[index] = i - index
            st.append(i)
        
        return ans