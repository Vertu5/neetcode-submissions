class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # Stores the character and its most recent index
        left = 0             # Left boundary of our sliding window
        max_length = 0       # Tracks the longest valid substring

        for right in range(len(s)):
            current_char = s[right]
            
            # If we've seen this character AND its last seen position is inside our current window
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Move the left boundary of the window to the right of the duplicate
                left = char_index_map[current_char] + 1
            
            # Update the character's most recent index to the current right pointer
            char_index_map[current_char] = right
            
            # Calculate the length of the current window and update max_length
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length