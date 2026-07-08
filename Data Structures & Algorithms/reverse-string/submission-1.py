class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        
        while i < j:
            # Pythonic swap using tuple unpacking
            s[i], s[j] = s[j], s[i]
            
            i += 1 
            j -= 1