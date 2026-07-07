class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_total = 0
        
        # On s'arrête à l'avant-dernier jour pour pouvoir comparer avec le lendemain
        for i in range(len(prices) - 1):
            
            # "J'achète quand c'est petit et je vends quand c'est grand"
            if prices[i + 1] > prices[i]:
                profit_total += prices[i + 1] - prices[i]
                
        return profit_total