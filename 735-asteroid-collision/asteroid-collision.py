class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                st.append(asteroids[i])
            else:
                while st and (asteroids[i]*-1)>st[-1] and st[-1]>0:
                    st.pop()
                # print(st)
                if st and (asteroids[i]*-1)==st[-1]:
                    # print('enter if')
                    st.pop()
                elif st==[] or st[-1]<0:
                    # print('enter elif')
                    st.append(asteroids[i])
                # print(st)
        return st