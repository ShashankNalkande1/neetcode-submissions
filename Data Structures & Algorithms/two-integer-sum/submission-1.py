class Solution:
    def twoSum(self, nums, target):
        
        # Dictionary to store numbers we have seen
        # key   -> number
        # value -> index of that number
        seen = {}
        
        
        # Loop through array using index
        for i in range(len(nums)):
            
            # Current number
            num = nums[i]
            
            
            # The number needed to reach the target
            needed = target - num
            
            
            # Check if we have already seen the needed number
            if needed in seen:
                
                # If yes, return indices
                return [seen[needed], i]
            
            
            # Otherwise store current number with its index
            seen[num] = i