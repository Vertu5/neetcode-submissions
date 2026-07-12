from collections import deque

class MyStack:

    def __init__(self):
        # On initialise une seule file (Queue)
        self.q = deque()
        
    def push(self, x: int) -> None:
        # 1. On ajoute le nouvel élément à la fin de la file
        self.q.append(x)
        
        # 2. L'astuce magique : on fait "tourner" la file
        # On prend tous les éléments qui étaient là avant 'x',
        # on les retire du début et on les remet à la fin.
        # Ainsi, 'x' se retrouve propulsé à l'avant de la file !
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
            
    def pop(self) -> int:
        # Comme notre 'push' a fait tout le travail de réorganisation,
        # le dernier élément ajouté est toujours à l'avant de la file.
        return self.q.popleft()

    def top(self) -> int:
        # On regarde l'élément à l'avant de la file sans le retirer
        return self.q[0]

    def empty(self) -> bool:
        # Retourne True si la file est vide, False sinon
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()