class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        debut = 0
        fin = len(nums) - 1

        # Le <= permet de gérer tout seul les listes à 1 élément 
        # et le moment où les pointeurs se croisent
        while debut <= fin:
            
            # Si l'élément de fin est la valeur à enlever, on le recule
            if nums[fin] == val:
                fin -= 1
                continue

            # Si l'élément de début est la valeur à enlever, 
            # on l'écrase avec celui de fin, puis on bouge les deux
            if nums[debut] == val:
                nums[debut] = nums[fin]
                debut += 1
                fin -= 1
                continue

            # Si l'élément de début est bon, on avance simplement
            debut += 1

        # 'debut' a avancé à chaque fois qu'un bon élément a été validé.
        # Il contient donc exactement le nombre 'k' demandé !
        return debut