class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        freq.sort()
        gaps = freq[25] - 1
        idle = gaps*n

        for i in range(24,-1,-1):
            idle -= min(gaps, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)