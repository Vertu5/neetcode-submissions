class Solution:
    def mySqrt(self, x: int) -> int:
        # Cas particulier pour 0
        if x == 0:
            return 0
            
        left = 1
        right = x
        
        while left <= right:
            middle = (left + right) // 2
            carre = middle * middle
            
            if carre == x:
                return middle
            elif carre > x:
                right = middle - 1
            else:
                left = middle + 1
                
        # Quand on sort de la boucle, 'right' contient l'arrondi inférieur
        return right