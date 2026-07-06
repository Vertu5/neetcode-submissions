class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        
        for string in strs:
            # sorted("b!aA") renvoie ['!', 'A', 'a', 'b']
            # "".join() recolle la liste pour faire la chaîne "!Aab"
            cle_verrouillee = "".join(sorted(string))
            
            hashmap.setdefault(cle_verrouillee, []).append(string)
                
        return list(hashmap.values())