class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                # On accumule le chiffre (pour gérer les nombres comme '12', '300', etc.)
                current_num = current_num * 10 + int(char)
                
            elif char == '[':
                # On met en pause : on sauvegarde la chaîne et le nombre construits jusque-là
                stack.append((current_string, current_num))
                # On réinitialise pour lire ce qui se trouve à l'intérieur des crochets
                current_string = ""
                current_num = 0
                
            elif char == ']':
                # La pause est finie : on récupère l'état précédent
                prev_string, num = stack.pop()
                # On multiplie ce qu'on vient de lire, et on l'ajoute à ce qu'on avait avant
                current_string = prev_string + current_string * num
                
            else:
                # C'est une lettre normale, on l'ajoute à la chaîne courante
                current_string += char
                
        return current_string