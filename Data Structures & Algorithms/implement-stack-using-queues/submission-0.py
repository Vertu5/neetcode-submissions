class MyStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        # On ajoute le "return" pour renvoyer la valeur supprimée
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def empty(self) -> bool:
        # Retourne True si la liste est vide, False si elle contient des éléments
        return len(self.stack) == 0
        # (return not self.stack)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()