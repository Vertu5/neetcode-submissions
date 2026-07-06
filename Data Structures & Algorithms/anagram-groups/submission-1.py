class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        
        for string in strs:
            compteur = {}
            # On compte dynamiquement ce qui se trouve dans le mot
            for char in string:
                compteur[char] = compteur.get(char, 0) + 1
            
            # compteur.items() ressemble à dict_items([('a', 2), ('!', 1)])
            # On le trie et on le fige en tuple : (('!', 1), ('a', 2))
            cle_verrouillee = tuple(sorted(compteur.items()))
            
            hashmap.setdefault(cle_verrouillee, []).append(string)
                
        return list(hashmap.values())