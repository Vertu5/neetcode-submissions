class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Représente notre "fenêtre" des k derniers éléments
        window = set() 

        for i, num in enumerate(nums):
            # 1. Si le nombre est dans notre fenêtre, on a trouvé un doublon proche !
            if num in window:
                return True
            
            # 2. Sinon, on l'ajoute à la fenêtre
            window.add(num)
            
            # 3. Si notre fenêtre devient plus grande que k, 
            # on retire l'élément le plus ancien pour la faire "glisser"
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False