class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        i = 0
        n = len(intervals)

        # 1. Trouver l'indice où commence le chevauchement (Phase AVANT)
        while i < n and intervals[i][1] < newInterval[0]:
            i += 1
        
        start = i # On mémorise le début de la zone à remplacer
        
        # 2. Trouver la fin du chevauchement et construire le "super-intervalle"
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # i est maintenant l'indice du premier intervalle strictement APRÈS.
        # 3. On remplace toute la zone de chevauchement [start:i] par le nouvel intervalle.
        # S'il n'y a eu aucun chevauchement, cela agit comme une simple insertion.
        intervals[start:i] = [newInterval]
        
        return intervals