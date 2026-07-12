class MinStack:

    def __init__(self):
        # La pile stockera des tuples sous la forme : (valeur, minimum_actuel)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # Si la pile est vide, l'élément est forcément le minimum
            self.stack.append((val, val))
        else:
            # On regarde quel était le minimum juste avant d'ajouter le nouvel élément
            current_min = self.stack[-1][1]
            # Le nouveau minimum est le plus petit entre le minimum précédent et la nouvelle valeur
            new_min = min(val, current_min)
            self.stack.append((val, new_min))

    def pop(self) -> None:
        # On retire simplement l'élément du dessus (et son minimum associé disparaît avec lui)
        self.stack.pop()

    def top(self) -> int:
        # On retourne la valeur (l'index 0 du tuple)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # On retourne le minimum (l'index 1 du tuple)
        return self.stack[-1][1]