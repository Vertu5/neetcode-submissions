class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0.0 # Garde en mémoire le temps du "bouchon" actuel
        
        for p, s in cars:
            time = (target - p) / s
            
            # Si cette voiture est plus lente que le bouchon devant elle, 
            # elle ne le rattrapera jamais. Elle crée sa propre flotte.
            if time > max_time:
                fleets += 1
                max_time = time # Elle devient le nouveau bouchon pour les suivants
                
        return fleets