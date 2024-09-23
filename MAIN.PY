class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Store numbers in a set for O(1) lookups
        longest_streak = 0
        
        for num in num_set:
            # Check if it is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count the length of the consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

# Example usage
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9

