class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(arr, low, mid, high):
            t = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    t.append(arr[left])
                    left += 1
                else:
                    t.append(arr[right])
                    right += 1
            while left <= mid:
                t.append(arr[left])
                left += 1
            while right <= high:
                t.append(arr[right])
                right += 1

            for i in range(low, high + 1):
                arr[i] = t[i - low]

        def countpairs(arr, low, mid, high):
            right = mid + 1
            ct = 0
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                ct += (right - (mid + 1))
            return ct

        def mergesort(arr, low, high):
            ct = 0
            if low >= high:
                return ct
            mid = (low + high) // 2
            ct += mergesort(arr, low, mid)
            ct += mergesort(arr, mid + 1, high)
            ct += countpairs(arr, low, mid, high)
            merge(arr, low, mid, high)
            return ct

        return mergesort(nums, 0, len(nums) - 1)
