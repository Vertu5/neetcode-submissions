class Solution:

    def pgcd(self, a, b):
        # tempo O(log(min(a, b))) parce que l'algorithme d'Euclide réduit les nombres de manière logarithmique
        while b != 0: 
            a, b = b, a % b # spatial O(1) car on ne fait que réassigner deux variables existantes
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # N = len(str1), M = len(str2)
        
        if not str1 or not str2 : # O(1)
            return ""

        # tempo O(N + M) parce que la concaténation et la comparaison parcourent les deux 
        # spatial O(N + M) parce que (str1 + str2) crée une nouvelle chaîne en mémoire de la taille totale
        if (str1 + str2 == str2 + str1): 

            size = self.pgcd(len(str1), len(str2)) # tempo O(log(min(N, M)))
            
            # tempo O(size) pour parcourir et couper la chaîne
            # spatial O(size) car le slicing crée une nouvelle sous-chaîne en mémoire
            window = str1[:size] 
            return window

        return ""