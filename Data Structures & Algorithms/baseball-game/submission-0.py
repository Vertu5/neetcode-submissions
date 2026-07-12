from typing import List

class Solution:
    def __init__(self):
        # On définit le dictionnaire des opérations comme un attribut de l'instance
        # Les lambdas prennent la pile (stack) et la modifient directement.
        self.operations = {
            "+": lambda stack: stack.append(stack[-1] + stack[-2]),
            "D": lambda stack: stack.append(stack[-1] * 2),
            "C": lambda stack: stack.pop()
        }

    def calPoints(self, ops: List[str]) -> int:
        # Le stack est réinitialisé à chaque nouvelle partie
        stack = []
        
        for op in ops:
            if op in self.operations:
                # Si c'est un symbole connu, on applique la règle associée au stack
                self.operations[op](stack)
            else:
                # Sinon, on ajoute le nombre au stack
                stack.append(int(op))
                
        # On retourne la somme de tous les éléments restants
        return sum(stack)