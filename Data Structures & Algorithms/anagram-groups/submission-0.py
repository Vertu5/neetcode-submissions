from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for string in strs:
            keys = [0] * 26
            for letter in string:
                keys[ord(letter) - ord("a")] += 1
            
            hashmap[tuple(keys)].append(string)
                
        return list(hashmap.values())