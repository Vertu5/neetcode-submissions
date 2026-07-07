from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialisation au Jour 0 (le tout premier jour)
        
        # Si on finit le jour 0 sans action, notre profit est de 0
        cash = 0 
        
        # Si on finit le jour 0 avec une action, on a dû l'acheter, 
        # donc on est en "dette" (profit négatif)
        hold = -prices[0] 
        
        # On parcourt les jours suivants
        for i in range(1, len(prices)):
            
            # Calcul des nouveaux états pour aujourd'hui
            # Vendre l'action (hold + prix) ou ne rien faire (cash)
            nouveau_cash = max(cash, hold + prices[i])
            
            # Acheter l'action (cash - prix) ou garder celle qu'on a (hold)
            nouveau_hold = max(hold, cash - prices[i])
            
            # Mise à jour pour le jour suivant
            cash = nouveau_cash
            hold = nouveau_hold
            
        # À la toute fin, pour avoir le profit maximum absolu, 
        # il vaut toujours mieux ne plus avoir d'action en main (cash)
        return cash