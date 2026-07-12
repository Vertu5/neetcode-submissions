class StockSpanner:
    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        span = 1
        idx = len(self.prices) - 1
        
        # Tant qu'on n'est pas au début et que le prix pointé est plus petit
        while idx >= 0 and self.prices[idx] <= price:
            # On ajoute le span de ce jour au nôtre
            span += self.spans[idx]
            # On FAIT UN SAUT en arrière en évitant les jours déjà validés
            idx -= self.spans[idx]
            
        self.prices.append(price)
        self.spans.append(span)
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)