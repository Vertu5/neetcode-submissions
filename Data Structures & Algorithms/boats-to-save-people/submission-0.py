class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # 1. Le tri est le cœur de la stratégie pour utiliser notre greedy
        people.sort()
        
        gauche = 0
        droite = len(people) - 1
        bateaux = 0
        
        while gauche <= droite:
            # On essaie d'associer le plus léger et le plus lourd notre greedy
            if people[gauche] + people[droite] <= limit:
                # Ils rentrent tous les deux !
                gauche += 1
                droite -= 1
            else:
                # Le plus lourd est trop gros, il part seul.
                # Le pointeur gauche (plus léger) ne bouge pas, il attend le prochain lourd.
                droite -= 1
                
            # Dans tous les cas (1 ou 2 personnes), un bateau vient de partir.
            bateaux += 1
            
        return bateaux