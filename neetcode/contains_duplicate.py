from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if an array contains any duplicate integers.
        
        Approach: Hash Set — store seen numbers, check membership in O(1).
        
        Time Complexity:  O(n) — one pass through the array.
        Space Complexity: O(n) — set can grow to size n in worst case.
        
        Args:
            nums: List of integers to check.
        Returns:
            True if any duplicate exists, False otherwise.
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False
