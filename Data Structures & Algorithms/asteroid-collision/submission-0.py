from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            # Variable pour savoir si l'astéroïde actuel a été détruit
            ast_exploded = False
            
            # Tant qu'il y a une collision: pile non vide, sommet positif, nouveau négatif
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < -ast:
                    # L'astéroïde de la pile est plus petit : il explose.
                    # On le retire et la boucle continue pour tester le suivant.
                    stack.pop()
                elif stack[-1] == -ast:
                    # Ils sont de même taille : les deux explosent.
                    stack.pop()
                    ast_exploded = True
                    break # L'astéroïde actuel est détruit, on sort de la boucle
                else:
                    # L'astéroïde de la pile est plus gros : l'astéroïde actuel explose.
                    ast_exploded = True
                    break # On sort de la boucle
            
            # Si l'astéroïde actuel a survécu à toutes les collisions (ou s'il n'y en a pas eu),
            # on l'ajoute à la pile.
            if not ast_exploded:
                stack.append(ast)
                
        return stack