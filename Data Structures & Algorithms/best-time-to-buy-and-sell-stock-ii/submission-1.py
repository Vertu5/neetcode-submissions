class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_total = 0
        i = 0
        n = len(prices)
        
        while i < n - 1:
            
            # 1. Chercher la vallée (le bon moment pour ACHETER)
            # TANT QUE le prix de demain est plus petit, on avance sans acheter
            while i < n - 1 and prices[i + 1] <= prices[i]:
                i += 1
            achat = prices[i]
            
            # 2. Chercher le pic (le bon moment pour VENDRE)
            # TANT QUE le prix de demain est plus grand, on garde l'action et on avance
            while i < n - 1 and prices[i + 1] > prices[i]:
                i += 1
            vente = prices[i]
            
            # 3. On encaisse le profit de ce mouvement
            profit_total += vente - achat
            
        return profit_total