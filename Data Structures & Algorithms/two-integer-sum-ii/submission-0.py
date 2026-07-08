class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 1. Initialisation aux extrémités
        gauche = 0
        droite = len(numbers) - 1
        
        # 2. Rapprochement des pointeurs
        while gauche < droite:
            somme_actuelle = numbers[gauche] + numbers[droite]
            
            if somme_actuelle == target:
                # Attention : le résultat doit être 1-indexed !
                return [gauche + 1, droite + 1]
                
            elif somme_actuelle < target:
                # La somme est trop petite, on augmente la valeur de gauche
                gauche += 1
                
            else:
                # La somme est trop grande, on diminue la valeur de droite
                droite -= 1

        return []