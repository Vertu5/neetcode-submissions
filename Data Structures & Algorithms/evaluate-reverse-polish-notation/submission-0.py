class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pile = []
        
        # 1. On crée notre dictionnaire d'opérations
        # lambda a, b : a + b signifie "une fonction qui prend a et b et retourne a + b"
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)  # On n'oublie pas le int() pour la division !
        }

        for i in tokens:
            # 2. Si le token est un opérateur (donc une clé de notre dictionnaire)
            if i in operations:
                under = pile.pop()
                above = pile.pop()
                
                # 3. LA MAGIE EST ICI :
                # operations[i] récupère la fonction correspondante (ex: la lambda du +)
                # et on lui passe nos deux nombres entre parenthèses.
                current = operations[i](above, under)
                
                pile.append(current)
            else:
                # Si ce n'est pas un opérateur, c'est un nombre
                pile.append(int(i))

        return pile.pop()