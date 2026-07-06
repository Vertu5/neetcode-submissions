from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # 1. Initialize to infinity so the first string's length takes over
        smallest = float('inf')
        res = ""

        # Find the length of the shortest string
        for s in strs:
            if not s:
                return res
            
            smallest = len(s) if len(s) < smallest else smallest 
        
        # Vertically scan characters up to the length of the shortest string
        for i in range(smallest):
            element = strs[0][i]
            for s in strs: 
                if s[i] != element:
                    return res
                
            res += element

        return res