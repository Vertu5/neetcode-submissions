import math

class Solution:
    def _build_frequencies(self, people: list[int], limit: int) -> list[int]:
        """
        Creates a 'bucket' for every possible weight.
        Index = weight, Value = number of people with that weight.
        """
        frequencies = [0] * (limit + 1)
        for weight in people:
            frequencies[weight] += 1
        return frequencies

    def _pair_different_weights(self, frequencies: list[int], left_weight: int, right_weight: int) -> int:
        """
        Pairs as many people as possible from two different weight groups.
        Returns the number of boats used.
        """
        # The number of pairs is limited by whichever group has fewer people
        pairs = min(frequencies[left_weight], frequencies[right_weight])
        
        # Remove the paired people from our buckets
        frequencies[left_weight] -= pairs
        frequencies[right_weight] -= pairs
        
        return pairs

    def _pack_same_weight(self, count: int, weight: int, limit: int) -> int:
        """
        Calculates boats needed for a group of people who all weigh the exact same.
        """
        # Can two people of this exact weight fit in one boat safely?
        if weight * 2 <= limit:
            # Yes: 2 people per boat (use math.ceil to round up for any odd person out)
            return math.ceil(count / 2)
        else:
            # No: they are too heavy to share, 1 person per boat
            return count

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # 1. Group everyone by weight instead of sorting the array
        frequencies = self._build_frequencies(people, limit)
        
        boats = 0
        left_weight = 1       # Lightest possible weight
        right_weight = limit  # Heaviest possible weight
        
        # 2. Process pairs of different weights
        while left_weight < right_weight:
            
            # Skip weights that have no people in them
            if frequencies[left_weight] == 0:
                left_weight += 1
                continue
            if frequencies[right_weight] == 0:
                right_weight -= 1
                continue
                
            # If the heaviest available can't even sit with the lightest available
            if left_weight + right_weight > limit:
                # All people at this heavy weight must take a boat alone
                boats += frequencies[right_weight]
                frequencies[right_weight] = 0
                right_weight -= 1
                
            else:
                # They can share! Let's pair up as many as we can in bulk
                boats += self._pair_different_weights(frequencies, left_weight, right_weight)
                
                # If a weight group is now empty, move its pointer
                if frequencies[left_weight] == 0:
                    left_weight += 1
                if frequencies[right_weight] == 0:
                    right_weight -= 1
                    
        # 3. Final Cleanup: Process anyone left over at the exact middle weight
        # (This happens when left_weight == right_weight)
        if frequencies[left_weight] > 0:
            boats += self._pack_same_weight(frequencies[left_weight], left_weight, limit)
            
        return boats