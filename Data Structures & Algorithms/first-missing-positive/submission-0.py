class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Passage 1 : Le tri cyclique (Cyclic Sort)
        for i in range(n):
            # 1. Le nombre doit être "utile" (entre 1 et n)
            # 2. Le nombre n'est pas déjà à sa place parfaite (nums[i] != nums[nums[i] - 1])
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # On détermine l'index où le nombre actuel DOIT aller
                correct_idx = nums[i] - 1
                
                # On fait l'échange (swap) en Python
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Passage 2 : Trouver le premier trou (le premier index mal rangé)
        for i in range(n):
            # Si la case 'i' ne contient pas 'i + 1', on a trouvé notre manquant !
            if nums[i] != i + 1:
                return i + 1
                
        # Cas extrême : si le tableau était parfait (ex: [1, 2, 3, 4])
        return n + 1