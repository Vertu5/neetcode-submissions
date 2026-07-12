class Solution:
    def __init__(self):
        # On garde l'index comme variable d'état de l'objet
        self.index = 0

    def decodeString(self, s: str) -> str:
        # On réinitialise l'index à chaque nouvel appel de la méthode publique 
        # (bonne pratique si l'objet est réutilisé pour plusieurs chaînes)
        self.index = 0
        return self._decode_recursive(s)

    def _decode_recursive(self, s: str) -> str:
        current_string = ""
        current_num = 0

        # On boucle tant qu'on n'a pas atteint la fin de la chaîne
        while self.index < len(s):
            char = s[self.index]
            self.index += 1  # On avance d'un pas quoiqu'il arrive

            if char.isdigit():
                # On accumule le nombre
                current_num = current_num * 10 + int(char)

            elif char == '[':
                # Appel récursif pour résoudre l'intérieur.
                # Grâce à self.index, la méthode appelée continuera là où on s'est arrêté.
                interieur_decode = self._decode_recursive(s)
                
                # On applique la multiplication
                current_string += interieur_decode * current_num
                current_num = 0  # Reset du multiplicateur

            elif char == ']':
                # On a trouvé la fin de la poupée russe actuelle.
                # On s'arrête là et on renvoie le résultat à la fonction parente.
                return current_string

            else:
                # Lettre normale
                current_string += char

        # Fin de la chaîne globale
        return current_string