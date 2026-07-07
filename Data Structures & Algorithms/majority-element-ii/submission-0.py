from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        # Phase 1 : L'élection (Trouver au maximum 2 suspects)
        candidat1, candidat2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            # Règle d'or : Toujours vérifier l'identité AVANT de vérifier si une chaise est vide
            if num == candidat1:
                count1 += 1
            elif num == candidat2:
                count2 += 1
            elif count1 == 0:
                candidat1 = num
                count1 = 1
            elif count2 == 0:
                candidat2 = num
                count2 = 1
            else:
                # Le nombre est différent des deux candidats et les deux chaises sont prises
                count1 -= 1
                count2 -= 1

        # Phase 2 : Le dépouillement (Compter les occurrences réelles des suspects)
        verify_count1, verify_count2 = 0, 0
        for num in nums:
            if num == candidat1:
                verify_count1 += 1
            elif num == candidat2:
                verify_count2 += 1

        # Phase 3 : Le verdict
        result = []
        n = len(nums)
        if verify_count1 > n // 3:
            result.append(candidat1)
        if verify_count2 > n // 3:
            result.append(candidat2)

        return result