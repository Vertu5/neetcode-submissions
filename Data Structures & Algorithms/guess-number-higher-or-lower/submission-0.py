# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # On cherche entre le nombre 1 et le nombre n
        left = 1
        right = n
        
        while left <= right:
            middle = (left + right) // 2
            
            # On pose la question à l'API pour notre milieu
            resultat = guess(middle)
            
            if resultat == 0:
                # Bingo, on a trouvé le bon nombre !
                return middle
                
            elif resultat == 1:
                # La cible est plus GRANDE que 'middle', on cherche à droite
                left = middle + 1
                
            else:
                # resultat == -1 : La cible est plus PETITE que 'middle', on cherche à gauche
                right = middle - 1