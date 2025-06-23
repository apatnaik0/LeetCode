class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in num:

            while st and k>0 and int(i)<int(st[-1]):
                st.pop()
                k-=1
            st.append(i)
        
        if k>0:
            st = st[0:-k]
        ans = ''.join(st).lstrip('0')
        return ans if ans else '0'
        