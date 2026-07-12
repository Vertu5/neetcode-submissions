class Solution:
    def __init__(self):
        # Notre Hashmap : on associe chaque ouvrante à la fermante qu'on ATTEND
        self.attendu = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

    def isValid(self, s: str) -> bool:
        stack = [] # Notre tableau qui sert de pile (pour le "pop")
        
        for char in s:
            # 1. "Si on voit un ouvert, on ajoute un fermé"
            if char in self.attendu:
                stack.append(self.attendu[char])
                
            # 2. Sinon (c'est un fermé), on pop et on vérifie
            else:
                # Si le stack est vide (ex: la chaîne commence par "]")
                # OU si le caractère qu'on dépile ne correspond pas à ce qu'on lit
                if not stack or stack.pop() != char:
                    return False
                    
        # À la fin, si le stack est vide, c'est que tout a été fermé correctement
        return len(stack) == 0