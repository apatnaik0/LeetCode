class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Keep original index
        arr = []
        for i in range(n):
            start, end, weight = intervals[i]
            arr.append([start, end, weight, i])

        # Sort by start time
        arr.sort(key=lambda x: x[0])

        # starts array for manual binary search
        starts = [arr[i][0] for i in range(n)]

        # next_idx[i] = first interval whose start > arr[i][1]
        next_idx = [n] * n

        for i in range(n):
            target = arr[i][1]

            l = i + 1
            r = n - 1
            ans = n

            while l <= r:
                mid = (l + r) // 2

                if starts[mid] > target:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1

            next_idx[i] = ans

        # dp[i][k] = (best_score, chosen_indices)
        # using intervals from i onward, with at most k picks
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        # Build from right to left
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Option 1: skip
                skip_score, skip_indices = dp[i + 1][k]

                # Option 2: take
                future_score, future_indices = dp[next_idx[i]][k - 1]

                curr_weight = arr[i][2]
                original_idx = arr[i][3]

                take_score = curr_weight + future_score
                take_indices = tuple(
                    sorted((original_idx,) + future_indices)
                )

                # Choose better option
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)

                else:
                    # same score -> lexicographically smaller
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)

        return list(dp[0][4][1])
        