class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # On découpe le chemin par les slash. 
        # Cela gère automatiquement les slash multiples qui deviennent des chaînes vides ''.
        for part in path.split("/"):
            if part == "..":
                # On remonte d'un dossier si on peut
                if stack:
                    stack.pop()
            elif part and part != ".":
                # 'part' vérifie que ce n'est pas vide (gère les '//')
                # 'part != "."' ignore le répertoire courant
                stack.append(part)
                
        # On reconstruit le chemin final
        return "/" + "/".join(stack)