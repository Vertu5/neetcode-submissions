class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # On crée une route vide où chaque index est un kilomètre
        # (On initialise avec 0 car un temps de trajet est toujours > 0)
        times = [0] * target
        
        # On "pose" chaque voiture sur la route avec son temps d'arrivée
        for p, s in zip(position, speed):
            times[p] = (target - p) / s
            
        fleets = 0
        max_time = 0.0
        
        # On parcourt la route de la ligne d'arrivée vers le départ
        for i in range(target - 1, -1, -1):
            if times[i] > max_time:
                fleets += 1
                max_time = times[i]
                
        return fleets