from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in‑place instead.
        """
        i = m - 1          # last real element in nums1
        j = n - 1          # last element in nums2
        k = m + n - 1      # write pointer at the very end

        while j >= 0:                  # keep going until nums2 is exhausted
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]    # move bigger nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]    # move nums2[j]
                j -= 1
            k -= 1
