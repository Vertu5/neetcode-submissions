class Solution:
    def findMin(self, nums: list[int]) -> int:
        gauche = 0
        droite = len(nums) - 1
        
        while gauche < droite:
            mid = (gauche + droite) // 2
            
            # On compare le milieu avec l'extrémité droite
            if nums[mid] > nums[droite]:
                # Le minimum est strictement à droite de mid
                gauche = mid + 1
            else:
                # Le minimum est à gauche, ou bien c'est mid lui-même
                droite = mid
                
        # À la fin de la boucle, gauche et droite pointent sur le minimum
        return nums[gauche]