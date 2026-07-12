class StockSpanner:
    """
    Implémentation optimisée utilisant le concept de "Pile Monotone" (Monotonic Stack).
    L'idée est de conserver uniquement les jours pertinents en condensant l'historique.

    Complexité Temporelle : 
    - Par appel à next() : $O(1)$ en moyenne (temps amorti).
      Explication : Bien qu'il y ait une boucle 'while', chaque prix ajouté au système 
      ne subit qu'un seul 'append()' et au maximum un seul 'pop()' tout au long de 
      sa durée de vie. Si l'on fait N appels à la fonction, la boucle while tournera 
      au maximum N fois au total. Le temps global est donc $O(N)$, ce qui donne un 
      temps moyen de $O(1)$ par appel.

    Complexité Spatiale :
    - $O(N)$ dans le pire des cas (où N est le nombre de prix traités).
      Explication : Le pire cas se produit si les prix arrivent dans un ordre 
      strictement décroissant (par exemple : 100, 90, 80, 70). Dans ce cas précis, 
      le sommet de la pile sera toujours plus petit que le nouveau prix, la boucle 
      while ne s'exécutera jamais, et on stockera chaque prix dans la pile.
    """

    def __init__(self):
        # On initialise notre pile. 
        # Elle contiendra des tuples sous la forme : (prix_du_jour, span_accumule)
        self.stack = []

    def next(self, price: int) -> int:
        # Le span de base pour le jour actuel est toujours d'au moins 1 (le jour lui-même)
        span = 1
        
        # On regarde en arrière pour "compresser" l'historique :
        # Tant que la stack n'est pas vide ET que le prix au sommet (index -1)
        # est inférieur ou égal au prix actuel que l'on traite.
        while self.stack and self.stack[-1][0] <= price:
            
            # On retire ce tuple obsolète de la stack et on récupère son span.
            # Il est obsolète car tout prix futur supérieur à cet ancien prix 
            # devra d'abord dépasser notre prix actuel.
            ancien_prix, ancien_span = self.stack.pop()
            
            # On absorbe l'historique (span) de l'élément retiré dans le nôtre.
            span += ancien_span
            
        # Une fois qu'on a "nettoyé" tous les prix plus petits, notre span 
        # contient la somme correcte. On ajoute le nouveau prix et son span total.
        self.stack.append((price, span))
        
        # On retourne le span calculé pour ce jour
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)