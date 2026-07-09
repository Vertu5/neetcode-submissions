class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Keeps track of unique characters in the current window
        left = 0          # The back pointer of our window
        max_length = 0    # Tracks our longest valid substring

        for right in range(len(s)):
            # If the character is already in our set, it's a duplicate.
            # We must shrink the window from the left until the duplicate is removed.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Now the window is valid again. Add the new character to the set.
            char_set.add(s[right])
            
            # Update the max length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length