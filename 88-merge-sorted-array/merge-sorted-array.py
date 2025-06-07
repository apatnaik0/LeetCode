class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=m-1
        r=n-1
        i = m+n-1
        while i>0 and r>=0 and l>=0:
            if nums2[r]>nums1[l]:
                nums1[i]=nums2[r]
                r-=1
            else:
                nums1[i]=nums1[l]
                l-=1
            i-=1
        while r>=0:
            nums1[i]=nums2[r]
            r-=1
            i-=1
        while l>=0:
            nums1[i]=nums1[l]
            l-=1
            i-=1

        