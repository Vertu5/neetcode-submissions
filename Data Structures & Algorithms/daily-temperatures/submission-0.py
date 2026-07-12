class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stocke les index des jours qui "cherchent" une température plus chaude
        
        for i, temp in enumerate(temperatures):
            # Dès qu'on trouve un jour plus chaud que celui au sommet de la pile
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()          # Ce jour précédent a trouvé sa réponse !
                res[prev_day] = i - prev_day    # On enregistre l'écart de jours
                
            # Le jour actuel rentre en salle d'attente
            stack.append(i)
            
        return res