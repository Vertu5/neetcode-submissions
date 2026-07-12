class Solution:
    def _computeMiddle(self, left: int, right: int) -> int:
        # Note : en C++ ou Java on écrirait "left + (right - left) // 2" pour 
        # éviter le dépassement, mais Python gère automatiquement les très grands nombres !
        return (left + right) // 2

    def search(self, nums: List[int], target: int) -> int:
        # Tes variables de départ
        left = 0
        right = len(nums) - 1

        # "Tant que la condition est vraie, je continue"
        while left <= right:
            # Le milieu se calcule automatiquement à chaque nouveau tour de boucle
            middle = self._computeMiddle(left, right)
            
            if target == nums[middle]:
                return middle  # On retourne l'index trouvé
            elif target > nums[middle]:
                left = middle + 1
            else: 
                right = middle - 1

        # Si on sort de la boucle sans avoir fait de "return", c'est qu'on n'a rien trouvé
        return -1