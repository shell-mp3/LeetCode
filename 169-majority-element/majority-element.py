class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        # First pass: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Second pass is optional if you're guaranteed a majority element exists
        return candidate
