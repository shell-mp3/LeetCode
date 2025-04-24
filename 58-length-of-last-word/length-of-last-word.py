class Solution:
    def lengthOfLastWord(self, s):
        # Step 1: Trim trailing spaces and split the string
        words = s.strip().split()
        
        # Step 2: Return the length of the last word
        return len(words[-1])
