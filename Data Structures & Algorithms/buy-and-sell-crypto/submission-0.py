class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # On initialise avec l'infini négatif pour le hold car 
        # on veut être sûr de prendre le premier prix au début
        cash = 0
        hold = -float('inf') 
        
        for price in prices:
            # 1. On vend l'action qu'on a (hold + price) ou on ne fait rien (cash)
            cash = max(cash, hold + price)
            
            # 2. On achète l'action POUR LA PREMIÈRE ET UNIQUE FOIS (-price)
            # ou on garde l'action qu'on avait déjà achetée avant (hold)
            hold = max(hold, -price)
            
        return cash