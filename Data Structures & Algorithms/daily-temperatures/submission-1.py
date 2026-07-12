class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        
        # On part de l'avant-dernier jour
        for i in range(n - 2, -1, -1):
            j = i + 1
            
            while j < n:
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                elif res[j] == 0:
                    # Si le jour j n'a aucun jour plus chaud dans son futur,
                    # et qu'il est plus froid que le jour i, alors i n'en aura pas non plus.
                    break
                else:
                    # Le fameux saut : on avance directement au prochain jour plus chaud que j
                    j += res[j]
                    
        return res