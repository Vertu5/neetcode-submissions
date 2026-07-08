class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialisation des 3 pointeurs
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Tant qu'il reste des éléments à comparer dans les deux tableaux
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1 # On recule le pointeur de positionnement dans tous les cas
            
        # Que se passe-t-il si on a épuisé nums1 mais qu'il reste des éléments dans nums2 ?
        # Il faut copier le reste de nums2 dans nums1.
        # (Si on a épuisé nums2 en premier, on n'a rien à faire car les éléments 
        # restants de nums1 sont déjà à leur bonne place !)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1