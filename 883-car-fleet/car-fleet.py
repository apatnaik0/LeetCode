class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        st = []
        cars = [[p,s] for p, s in zip(position, speed)]

        for p, s in sorted(cars)[::-1]:
            time = (target - p)/s
            if not st or st[-1] < time:
                st.append(time)
        return len(st)