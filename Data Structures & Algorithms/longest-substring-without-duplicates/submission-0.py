class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # HashMap to store {character: most recent index}
        left = 0       # The back pointer of our sliding window
        max_length = 0 

        for right in range(len(s)):
            current_char = s[right]
            
            # If we see a duplicate AND its last known index is inside our current window
            if current_char in char_map and char_map[current_char] >= left:
                # JUMP the left pointer directly past the previous occurrence
                left = char_map[current_char] + 1
            
            # Update the hashmap with the new, most recent index of the character
            char_map[current_char] = right
            
            # Calculate the max length
            max_length = max(max_length, right - left + 1)
            
        return max_length