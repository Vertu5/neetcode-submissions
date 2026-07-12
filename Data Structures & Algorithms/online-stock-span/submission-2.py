class StockSpanner:
    def __init__(self):
        # On ajoute un faux jour 0 ("-1") avec un prix infini pour éviter 
        # que la pile ne soit vide si on bat tous les records.
        self.stack = [(float('inf'), -1)]
        self.day_index = -1 # Compteur de jours

    def next(self, price: int) -> int:
        self.day_index += 1
        
        # On dépile tant que le prix est plus petit ou égal
        while self.stack[-1][0] <= price:
            self.stack.pop()
            
        # Le span est la distance entre aujourd'hui et le dernier jour "plus grand"
        span = self.day_index - self.stack[-1][1]
        
        self.stack.append((price, self.day_index))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)