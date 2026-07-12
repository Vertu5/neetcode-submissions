class MyQueue:

    def __init__(self):
        # On utilise des listes Python normales comme des Piles (Stacks)
        # On s'interdit d'utiliser pop(0), on n'a droit qu'à append() et pop()
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # On ajoute toujours les nouveaux éléments dans stack_in
        self.stack_in.append(x)

    def pop(self) -> int:
        # L'astuce : on appelle peek() pour s'assurer que stack_out a les bons éléments
        self.peek()
        # Puis on retire l'élément du dessus de stack_out (qui est le plus ancien)
        return self.stack_out.pop()

    def peek(self) -> int:
        #complexité amortie $O(1)$
        # Si le verre de sortie est vide, on doit aller chercher les éléments
        # dans le verre d'entrée et tout transvaser.
        if not self.stack_out:
            while self.stack_in:
                # On prend le haut de stack_in et on le met dans stack_out
                self.stack_out.append(self.stack_in.pop())
                
        # On regarde le haut de stack_out
        return self.stack_out[-1]

    def empty(self) -> bool:
        # La file est vide SEULEMENT SI les deux piles sont vides
        return not self.stack_in and not self.stack_out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()