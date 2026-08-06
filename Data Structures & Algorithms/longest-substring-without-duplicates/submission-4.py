class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maps character to its most recent index
        char_index_map = {} 
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # If we've seen the character AND its old position is inside our current window
            if char in char_index_map and char_index_map[char] >= left:
                # Teleport the left edge right past the duplicate
                left = char_index_map[char] + 1
            
            # Update the character's most recent index
            char_index_map[char] = right
            
            # Calculate the max length
            max_len = max(max_len, right - left + 1)
            
        return max_len