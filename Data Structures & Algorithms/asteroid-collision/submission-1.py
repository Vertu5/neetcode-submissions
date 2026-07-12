from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # Raccourci pythonique: "a < 0 < stack[-1]" remplace "a < 0 and stack[-1] > 0"
            while stack and a < 0 < stack[-1]:
                diff = a + stack[-1]
                
                if diff <= 0:
                    stack.pop()  # L'astéroïde de la pile explose
                    
                if diff >= 0:
                    a = 0        # Le nouvel astéroïde explose
                    
            if a:
                stack.append(a)
                
        return stack