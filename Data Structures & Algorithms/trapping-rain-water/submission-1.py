class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        # 1. Trouver le "centre" : l'index du mur le plus haut
        index_sommet = 0
        for i in range(len(height)):
            if height[i] > height[index_sommet]:
                index_sommet = i
                
        total_water = 0
        
        # 2. Remplir la partie GAUCHE (en allant vers le sommet)
        max_left = 0
        for i in range(index_sommet):
            if height[i] > max_left:
                max_left = height[i]
            else:
                total_water += max_left - height[i]
                
        # 3. Remplir la partie DROITE (en allant vers le sommet)
        max_right = 0
        # On part de la fin et on recule jusqu'au sommet
        for i in range(len(height) - 1, index_sommet, -1):
            if height[i] > max_right:
                max_right = height[i]
            else:
                total_water += max_right - height[i]
                
        return total_water